import sys
import os
 
# Add project root (parent of this file's folder) to the import path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
 
 
def main():
    try:
        from app.config.settings import settings
    except ImportError as e:
        print(f"❌ Could not import settings: {e}")
        print(f"   -> Looked for the 'app' package in: {PROJECT_ROOT}")
        print("      Check that app/config/settings.py actually exists there.")
        sys.exit(1)
    except KeyError as e:
        print(f"❌ Missing environment variable: {e}")
        print("   -> Check that a .env file exists in the project root")
        print("      and contains a line like: JWT_SECRET=your-secret-here")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Settings failed to load: {e}")
        sys.exit(1)
 
    print("✅ settings.py loaded successfully\n")
 
    checks = []
 
    # --- Application ---
    checks.append(("application.name", settings.application.name == "Rentify"))
    checks.append(("application.debug is bool", isinstance(settings.application.debug, bool)))
 
    # --- AI (no Database section: this service is stateless, Java owns storage) ---
    checks.append(("ai.blur_threshold is float", isinstance(settings.ai.blur_threshold, float)))
    checks.append(("ai.blur_normalize_edge is positive int", isinstance(settings.ai.blur_normalize_edge, int) and settings.ai.blur_normalize_edge > 0))
 
    # --- Redis (optional, may be None) ---
    if settings.redis is not None:
        checks.append(("redis.port is int", isinstance(settings.redis.port, int)))
    else:
        print("ℹ️  redis is None (that's fine — it's Optional)")
 
    # --- Security / JWT ---
    checks.append(("security.jwt_secret is non-empty str", bool(settings.security.jwt_secret) and isinstance(settings.security.jwt_secret, str)))
    checks.append(("security.jwt_algorithm == HS256", settings.security.jwt_algorithm == "HS256"))
    checks.append(("security.access_token_expire is int", isinstance(settings.security.access_token_expire, int)))
    checks.append(("security.access_token_expire > 0", settings.security.access_token_expire > 0))
 
    # --- Logging ---
    checks.append(("logging.level is str", isinstance(settings.logging.level, str)))
 
    # --- Print results ---
    all_passed = True
    for label, passed in checks:
        status = "✅" if passed else "❌"
        if not passed:
            all_passed = False
        print(f"{status} {label}")
 
    print()
    if all_passed:
        print("🎉 All checks passed. Your settings.py is working correctly.")
    else:
        print("⚠️  Some checks failed — see above.")
        sys.exit(1)
 
    # Extra: show (masked) JWT secret so you can eyeball it without leaking it fully
    secret = settings.security.jwt_secret
    masked = secret[:4] + "..." + secret[-4:] if len(secret) > 8 else "****"
    print(f"\nJWT secret loaded (masked): {masked}")
    print(f"JWT algorithm: {settings.security.jwt_algorithm}")
    print(f"Access token expire (ms): {settings.security.access_token_expire}")
 
 
if __name__ == "__main__":
    main()
 