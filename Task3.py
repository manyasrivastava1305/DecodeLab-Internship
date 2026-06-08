# DecodeLabs Industrial Training Kit - Project 3
# Module Name: enterprise_password_generator.py
# Description: A cryptographically secure, enterprise-grade Random Password Generator
#              built using an Input-Process-Output architectural scaffold[cite: 6, 75].
#              Adheres to NIST 2024 (SP 800-63-4) password length standards [cite: 94]
#              and ensures O(N) memory efficiency[cite: 148].
# Author: Manya Srivastava
# Batch: 2026 [cite: 4]

# =====================================================================
# LIBRARY INTEGRATION
# =====================================================================
# Professional engineering leverages verified, high-quality standard libraries [cite: 72]
import math
import secrets  # Mandatory enterprise standard for high-quality OS-level entropy [cite: 119, 120]
import string   # Provides locale-independent, error-free character classifications [cite: 102, 104]


# =====================================================================
# CONSTANTS & CONFIGURATION
# =====================================================================
# Defining clear validation bounds based on security guidelines [cite: 80]
MIN_PASSWORD_LENGTH = 12    # Balanced high-security minimum entry point
NIST_HIGH_SECURITY_MIN = 15 # NIST SP 800-63-4 recommended minimum for high-security [cite: 94]
MAX_PASSWORD_LENGTH = 64    # Maximum required standard length to support passphrases [cite: 94]


def calculate_information_entropy(length: int, pool_size: int) -> float:
    # Phase 3: The mathematical provision of security[cite: 154].
    # Calculates the statistical unpredictability of the string in bits[cite: 161].
    # Formula: E = L * log2(R) [cite: 162]
    # 
    # Args:
    #     length (int): Length of the generated password (L) [cite: 163]
    #     pool_size (int): Size of the character pool used (R) [cite: 164]
    #     
    # Returns:
    #     float: Entropy value evaluated in bits.
    
    if pool_size <= 0 or length <= 0:
        return 0.0
    return length * math.log2(pool_size)


def request_validated_length() -> int:
    # Phase 1: Defining environmental requirements and data validation[cite: 86].
    # Rigorously validates user input to capture a target integer and prevent
    # system crashes or fundamentally insecure structural setups[cite: 89, 90].
    # 
    # Returns:
    #     int: A thoroughly verified target password length.
    
    print("\n" + "="*60)
    print("      DECODELABS ENTERPRISE CREDENTIAL SECURITY ARCHITECTURE      ")
    print("="*60)
    
    while True:
        try:
            user_input = input(f"Enter target password length ({MIN_PASSWORD_LENGTH}-{MAX_PASSWORD_LENGTH}): ").strip()
            
            # Catch empty inputs
            if not user_input:
                print("[!] Input validation failure: Field cannot be empty.")
                continue
                
            length = int(user_input)
            
            # Bound validation to check against structural constraints [cite: 80, 90]
            if length < MIN_PASSWORD_LENGTH:
                print(f"[!] Security Exception: Length must be at least {MIN_PASSWORD_LENGTH} characters for baseline safety.")
                continue
            elif length > MAX_PASSWORD_LENGTH:
                print(f"[!] Buffer Exception: System restricts passphrase allocations to a maximum of {MAX_PASSWORD_LENGTH} characters[cite: 94].")
                continue
                
            return length
            
        except ValueError:
            print("[!] Critical Input Failure: Expected a valid mathematical integer[cite: 89].")


def generate_secure_password(length: int) -> tuple[str, int]:
    # Phase 2: Backend Transformation Engine[cite: 96].
    # Assembles standard character blocks and executes a random selection algorithm[cite: 99].
    # Replaces junior string concatenation += (O(N^2)) with join() (O(N)) to guarantee
    # peak memory efficiency and performance[cite: 140, 150, 152].
    # 
    # Args:
    #     length (int): The validated number of characters required[cite: 89].
    #     
    # Returns:
    #     tuple[str, int]: The cryptographically secure password string and character pool size.
    
    # Standardizing character blocks with the string library to ensure consistency [cite: 102, 104]
    letters = string.ascii_letters  # Concatenation of lowercase and uppercase ASCII [cite: 105]
    digits = string.digits          # The base string '0123456789' [cite: 106, 108]
    punctuation = string.punctuation # Standard ASCII symbols and punctuation marks [cite: 107, 109]
    
    # Pool composition: Combining pools to prioritize length over custom character constraints [cite: 92, 99]
    character_pool = letters + digits + punctuation
    pool_size = len(character_pool)
    
    # O(N) Enterprise Accumulator Pattern [cite: 140, 145]
    # Uses secrets.choice() for hardware-level noise generation, bypassing predictable seed states [cite: 120, 121]
    password_list = [secrets.choice(character_pool) for _ in range(length)]
    
    # Single memory allocation operation avoiding quadratic replication impacts [cite: 137, 152]
    secure_password = "".join(password_list)
    
    return secure_password, pool_size


def display_security_provision(password: str, pool_size: int) -> None:
    # Phase 3: Secure Delivery and Output Assessment.
    # Outputs the final structural provisioning and delivers a mathematical evaluation
    # of its resistance against modern GPU-accelerated cracking operations.
    
    length = len(password)
    entropy_bits = calculate_information_entropy(length, pool_size)
    
    print("\n" + "-"*60)
    print("                SECURE PROVISION DELIVERY ENGINE               ")
    print("-"*60)
    print(f"Generated Credential : {password}")
    print(f"Target Length (L)    : {length} characters [cite: 163]")
    print(f"Active Pool Size (R) : {pool_size} structural variations [cite: 164]")
    print(f"Information Entropy  : {entropy_bits:.2f} bits of cryptographic resistance [cite: 161]")
    print("-"*60)
    
    # Structural risk assessment against hardware clusters testing billions of keys per second [cite: 168]
    print("NIST Architectural Status Evaluation:")
    if length >= NIST_HIGH_SECURITY_MIN:
        print(f"  [+] STATUS: Compliant with NIST 2024 standards for high-security environments[cite: 94].")
    else:
        print(f"  [-] STATUS: Standard validation achieved. Upgrade to >= {NIST_HIGH_SECURITY_MIN} for high-security pipelines[cite: 94].")
        
    if entropy_bits >= 128:
        print("  [+] ENTROPY LEVEL: Exceptional. Resistant to nation-state level brute force setups.")
    elif entropy_bits >= 80:
        print("  [+] ENTROPY LEVEL: Strong. Secure against modern commercial multi-GPU clusters[cite: 168].")
    else:
        print("  [!] ENTROPY LEVEL: Marginal. Increase character count to scale algorithmic strength[cite: 165].")
    print("="*60 + "\n")


def main() -> None:
    # Orchestrates the structural Input-Process-Output engine scaffold[cite: 75].
    # Defines execution lifecycles safely across terminal scopes.
    
    try:
        # 1. Input Validation Phase [cite: 77, 86]
        target_length = request_validated_length()
        
        # 2. Logic Processing Transformation Engine Phase [cite: 78, 96]
        secure_credential, pool_size = generate_secure_password(target_length)
        
        # 3. Controlled Output Pipeline Phase [cite: 79, 83]
        display_security_provision(secure_credential, pool_size)
        
    except KeyboardInterrupt:
        print("\n\n[!] System Execution Halted: Secure runtime process terminated by user request.")
    except Exception as e:
        print(f"\n[!] Critical System Interruption: {str(e)}")


if __name__ == "__main__":
    main()
