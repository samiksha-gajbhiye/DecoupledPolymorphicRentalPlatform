package com.sg.main.services;

import java.time.Duration;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;

import com.sg.main.dto.SearchHit;
import com.sg.main.dto.python.RankedItem;
import com.sg.main.dto.python.SearchItem;
import com.sg.main.dto.python.SearchRankRequest;
import com.sg.main.dto.python.SearchRankResponse;
import com.sg.main.entities.Product;
import com.sg.main.repositories.ProductRepository;

@Service
public class ProductSearchService {

    private static final Logger log = LoggerFactory.getLogger(ProductSearchService.class);
    private static final int MAX_ITEMS = 1000;
    private static final int TOP_K = 50;

    @Autowired
    private ProductRepository productRepository;

    @Autowired
    private WebClient pythonWebClient;

    @Value("${python.service.timeout-seconds:20}")
    private long timeoutSeconds;

    public List<SearchHit> search(String query) {
        String q = query == null ? "" : query.trim();
        if (q.isEmpty()) {
            return List.of();
        }

        List<Product> products = productRepository.findAll();
        if (products.isEmpty()) {
            return List.of();
        }
        if (products.size() > MAX_ITEMS) {
            products = products.subList(0, MAX_ITEMS);
        }

        try {
            return semanticSearch(q, products);
        } catch (Exception e) {
            log.warn("Semantic search unavailable, using keyword fallback: {}", e.getMessage());
            return keywordSearch(q, products);
        }
    }

    private List<SearchHit> semanticSearch(String q, List<Product> products) {
        Map<Integer, Product> byId = new HashMap<>();
        List<SearchItem> items = new ArrayList<>();
        for (Product p : products) {
            byId.put(p.getProductId(), p);
            items.add(new SearchItem(p.getProductId(), searchableText(p)));
        }

        SearchRankResponse response = pythonWebClient.post()
                .uri("/search/rank")
                .bodyValue(new SearchRankRequest(q, items, TOP_K))
                .retrieve()
                .bodyToMono(SearchRankResponse.class)
                .timeout(Duration.ofSeconds(timeoutSeconds))
                .block();

        if (response == null || !response.success() || response.data() == null) {
            throw new IllegalStateException("Python returned no usable ranking");
        }

        List<SearchHit> hits = new ArrayList<>();
        for (RankedItem r : response.data().results()) {
            Product p = byId.get(r.id());
            if (p != null) {
                hits.add(new SearchHit(p, r.score(), r.strong()));
            }
        }
        return hits;
    }

    private List<SearchHit> keywordSearch(String q, List<Product> products) {
        String[] words = q.toLowerCase().split("\\s+");
        List<SearchHit> hits = new ArrayList<>();
        for (Product p : products) {
            String text = searchableText(p).toLowerCase();
            for (String w : words) {
                if (w.length() > 1 && text.contains(w)) {
                    hits.add(new SearchHit(p, 0.0, true));
                    break;
                }
            }
        }
        return hits;
    }

    private String searchableText(Product p) {
        StringBuilder sb = new StringBuilder();
        append(sb, p.getTitle());
        append(sb, p.getBrand());
        append(sb, p.getModel());
        append(sb, p.getCategory() != null ? p.getCategory().getName() : null);
        append(sb, p.getDescription());
        return sb.length() == 0 ? p.getTitle() : sb.toString();
    }

    private void append(StringBuilder sb, String part) {
        if (part != null && !part.isBlank()) {
            if (sb.length() > 0) {
                sb.append(". ");
            }
            sb.append(part.trim());
        }
    }
}
