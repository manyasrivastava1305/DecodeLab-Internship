# DecodeLabs Industrial Training Kit - Project 2
# Module Name: stateful_expense_tracker.py
# Description: An enterprise-grade, state-preserving Expense Tracker built using
#              the Input-Process-Output (IPO) architectural scaffold.
#              Tracks continuous transaction data points in an internal ledger
#              and generates a detailed final transaction audit report.
# Author: Manya Srivastava
# Batch: 2026

# =====================================================================
# CONSTANTS & CONFIGURATION
# =====================================================================
# Definitive loop control value to trigger a graceful termination sequence
SENTINEL_QUIT_VALUE = "quit"  # Sentinel value mapped to kill switch path


def process_transaction_ledger() -> tuple[float, list[float]]:
    # Phase 1 & 2: Structural Initialization and Stateful Ledger Processing
    # Instantiates the long-term memory buffers OUTSIDE the execution loop scope.
    # We maintain both a scalar accumulator (total) and a linear vector tracker (list).
    total_spent = 0.0             # Cumulative running balance memory block
    transaction_history = []      # Active array list to track individual transactions

    print("\n" + "="*60)
    print("        DECODELABS STATE-PRESERVING TRANSACTION ARCHITECTURE        ")
    print("="*60)
    print(f" Instructions: Enter numerical amounts sequentially.")
    print(f" Type '{SENTINEL_QUIT_VALUE}' to halt execution and view the audit summary.")
    print("-"*60)

    # The Continuous Audit Loop: Managing a live, real-time dataset workflow
    while True:  # Infinite execution cycle for real-time monitoring
        try:
            # Phase 1: Input Gathering and Sanitization
            raw_input = input("Enter transaction expense amount: ").strip()

            # The Kill Switch Evaluation: Intercepting the sentinel token string
            if raw_input.lower() == SENTINEL_QUIT_VALUE:  # Intercept path
                print("\n[+] Sentinel Intercepted: Graceful processing shutdown initiated.")
                break  # Break loop to trigger standard summary pipeline

            # Catch empty user inputs safely to prevent conversion anomalies
            if not raw_input:
                print("[!] Input validation exception: Entry field cannot be empty.")
                continue

            # Defensive Coding (Digital Poka-Yoke): Enforcing data conversion type-safety
            new_expense = float(raw_input)  # Transformation mechanism converting raw data feed

            # Enforcing transactional reality constraints
            if new_expense < 0:
                print("[!] Audit Warning: Negative value detected. Please enter absolute positive costs.")
                continue

            # Phase 2: Accumulator Mutation & Data Tracking Engine
            total_spent += new_expense                  # State calculation rule
            transaction_history.append(new_expense)     # Appending to transaction ledger track list
            
            # Real-time feedback showing current index state
            transaction_index = len(transaction_history)
            print(f"    [Success] Txn #{transaction_index} registered: ${new_expense:.2f} | Rolling Total: ${total_spent:.2f}")

        except ValueError:  # Catch block matching the digital barrier requirements
            # Catching invalid parsing blocks securely to preserve runtime state memory bank
            print(f"[!] Type Validation Error: '{raw_input}' is not a valid mathematical float.")
            print("    Garbage input dropped safely. Long-term memory state preserved.")

    return total_spent, transaction_history  # Return refined dynamic total and history ledger


def display_audit_presentation(final_total: float, history: list[float]) -> None:
    # Phase 3: Presentation and Decoupled Output Delivery
    # Decouples data processing layers cleanly from final console views.
    print("\n" + "-"*60)
    print("                REFINED TRANSACTION AUDIT REPORT                ")
    print("-"*60)
    print(f" Final Actionable Status : Processing Complete")
    print(f" Total Transactions Run  : {len(history)}")
    
    # Structural presentation of tracked ledger data
    print("\n Itemized Transaction Ledger Track:")
    if not history:
        print("   [None] No transactions were recorded during this execution session.")
    else:
        for idx, amount in enumerate(history, start=1):
            print(f"   Transaction #{idx:02d} : ${amount:.2f}")
            
    print("-"*60)
    print(f" Consolidated Expenditure: ${final_total:.2f}")
    print("-"*60)
    print(" INPUT. PROCESS. OUTPUT. TRUTH. - System validation confirmed.")
    print("="*60 + "\n")


def main() -> None:
    # Orchestrates execution lifecycles safely across terminal scopes.
    try:
        # 1. Trigger processing transformation engine via the interactive terminal
        calculated_total, tracked_history = process_transaction_ledger()

        # 2. Route structural provisioning data onto the output delivery interface
        display_audit_presentation(calculated_total, tracked_history)  # Prints final history and total

    except KeyboardInterrupt:
        print("\n\n[!] System Interruption: Secure financial stream forced offline by terminal request.")
    except Exception as e:
        print(f"\n[!] Critical Engineering Exception: {str(e)}")


if __name__ == "__main__":
    main()
