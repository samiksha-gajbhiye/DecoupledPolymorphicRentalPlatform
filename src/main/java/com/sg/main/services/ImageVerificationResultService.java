package com.sg.main.services;


import java.time.Duration;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.http.MediaType;
import org.springframework.http.client.MultipartBodyBuilder;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.reactive.function.BodyInserters;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.reactive.function.client.WebClientResponseException;

import com.sg.main.dto.python.VerifyData;
import com.sg.main.dto.python.VerifyResponse;
import com.sg.main.entities.ImageVerificationResult;
import com.sg.main.entities.ProductImage;
import com.sg.main.repositories.ImageVerificationResultRepository;

@Service
public class ImageVerificationResultService {

	 private static final Logger log = LoggerFactory.getLogger(ImageVerificationResultService.class);

	    @Autowired
	    private WebClient pythonWebClient;

	    @Autowired
	    private ImageVerificationResultRepository resultRepository;

	    @Value("${python.service.timeout-seconds:20}")
	    private long timeoutSeconds;

	    @Value("${verification.min-category-confidence:0.7}")
	    private double minCategoryConfidence;

	    /**
	     * Sends one image to Python and applies the pass/fail policy.
	     * Never throws: if Python is down, slow, or rejects the file, returns false
	     * so product registration is never blocked by the AI service.
	     */
	    public boolean verify(MultipartFile file, ProductImage savedImage, String expectedCategory) {
	        try {
	            String contentType = file.getContentType() != null
	                    ? file.getContentType() : MediaType.APPLICATION_OCTET_STREAM_VALUE;

	            MultipartBodyBuilder builder = new MultipartBodyBuilder();
	            builder.part("file", new ByteArrayResource(file.getBytes()) {
	                        @Override
	                        public String getFilename() {
	                            return file.getOriginalFilename();
	                        }
	                    })
	                    .contentType(MediaType.parseMediaType(contentType));

	            VerifyResponse response = pythonWebClient.post()
	                    .uri("/image/verify")
	                    .contentType(MediaType.MULTIPART_FORM_DATA)
	                    .body(BodyInserters.fromMultipartData(builder.build()))
	                    .retrieve()
	                    .bodyToMono(VerifyResponse.class)
	                    .timeout(Duration.ofSeconds(timeoutSeconds))
	                    .block();

	            if (response == null || !response.success() || response.data() == null) {
	                log.warn("Python returned no usable result for {}", file.getOriginalFilename());
	                return false;
	            }

	            VerifyData data = response.data();

	            boolean categoryMatches = data.category() != null
	                    && expectedCategory != null
	                    && data.category().equalsIgnoreCase(expectedCategory);

	            boolean passed = !data.blurry()
	                    && data.categoryConfidence() >= minCategoryConfidence
	                    && categoryMatches;

	            ImageVerificationResult result = new ImageVerificationResult();
	            result.setProductImage(savedImage);
	            result.setLabel(data.label());
	            result.setCategory(data.category());
	            result.setConfidence(data.confidence());
	            result.setCategoryConfidence(data.categoryConfidence());
	            result.setBlurry(data.blurry());
	            result.setBlurryScore(data.blurScore());
	            result.setPassed(passed);
	            resultRepository.save(result);

	            log.info("Verified {} -> category={}, conf={}, blurry={}, expected={}, passed={}",
	                    file.getOriginalFilename(), data.category(), data.categoryConfidence(),
	                    data.blurry(), expectedCategory, passed);

	            return passed;

	        } catch (WebClientResponseException e) {
	            log.warn("Python rejected {} ({}): {}", file.getOriginalFilename(),
	                    e.getStatusCode(), e.getResponseBodyAsString());
	            return false;
	        } catch (Exception e) {
	            log.warn("Image verification unavailable for {}: {}", file.getOriginalFilename(), e.getMessage());
	            return false;
	        }
	    }
}
