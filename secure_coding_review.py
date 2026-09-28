import logging
import re

logging.basicConfig(
    filename="security_report.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("[-] Starting Secure Coding Review & Audit Simulation...\n")
logging.info("Starting Secure Coding Review session.")

print("--- [Audit Test 1: Input Validation] ---")

def secure_process_input(user_input):
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(email_pattern, user_input):
        logging.info(f"Secure Input Validation Passed for: {user_input}")
        return "[+] Input is valid and safe."
    else:
        logging.warning(f"Invalid or malicious input attempt blocked: {user_input}")
        return "[-] Error: Invalid input format detected! Request blocked."

test_input = "test.user@codealpha.com"
result = secure_process_input(test_input)
print(result)

print("\n--- [Audit Test 2: Secure Error Handling] ---")

def secure_division(a, b):
    try:
        result = a / b
        return f"[+] Result: {result}"
    except ZeroDivisionError:
        logging.error("Exception handled: Division by zero attempted.")
        return "[-] Error: Cannot divide by zero. Please check your input."
    except Exception as e:
        logging.error(f"Unexpected error occurred: {str(e)}")
        return "[-] An unexpected system error occurred."

print(secure_division(10, 0))

print("\n[+] Audit completed successfully. Report saved to 'security_report.log'.")
logging.info("Secure Coding Review session completed successfully.")
