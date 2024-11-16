# import time
# import cv2
# from segmentation import *
# from coding import *
# from recognition import *

# # Function to compare iris codes
# def compare_codes(a, b, mask_a, mask_b, rotation=False):
#     if rotation:
#         d = []
#         for i in range(-rotation, rotation + 1):
#             c = np.roll(b, i, axis=1)
#             mask_c = np.roll(mask_b, i, axis=1)
#             d.append(np.sum(np.remainder(a + c, 2) * mask_a * mask_c) / np.sum(mask_a * mask_c))
#         return np.min(d)
#     return np.sum(np.remainder(a + b, 2) * mask_a * mask_b) / np.sum(mask_a * mask_b)

# # Function to encode the iris photo
# def encode_photo(image):
#     img = preprocess(image)
#     x, y, r = find_pupil_hough(img)
#     x_iris, y_iris, r_iris = find_iris_hough(img)
#     iris = unravel_iris(image, x, y, r, x_iris, y_iris, r_iris)
#     return iris_encode(iris)

# # ATM Class
# class ATM:
#     def __init__(self, balance=0, pin="1234"):
#         self.balance = balance
#         self.transaction_history = []
#         self.pin = pin  # Default pin is set to 1234 for simplicity

#     def verify_pin(self):
#         # Loop to verify the PIN. The user gets 3 attempts.
#         attempts = 3
#         while attempts > 0:
#             entered_pin = input("Enter your PIN: ")
#             if entered_pin == self.pin:
#                 print("PIN verified successfully!")
#                 return True
#             else:
#                 attempts -= 1
#                 print(f"Incorrect PIN. You have {attempts} attempts remaining.")
#                 if attempts == 0:
#                     print("No attempts remaining. Exiting...")
#                     return False
#         return False

#     def show_balance(self):
#         print(f"Your current balance is: ${self.balance}")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Please enter a valid amount to withdraw.")
#         elif amount > self.balance:
#             print("Insufficient funds.")
#         else:
#             self.balance -= amount
#             self.transaction_history.append(f"Withdrew: ${amount}")
#             print(f"Successfully withdrew ${amount}.")
#             self.show_balance()

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Please enter a valid amount to deposit.")
#         else:
#             self.balance += amount
#             self.transaction_history.append(f"Deposited: ${amount}")
#             print(f"Successfully deposited ${amount}.")
#             self.show_balance()

#     def print_transaction_history(self):
#         print("\nTransaction History:")
#         if not self.transaction_history:
#             print("No transactions yet.")
#         else:
#             for transaction in self.transaction_history:
#                 print(transaction)

# # Function to show the ATM menu
# def atm_menu():
#     print("\nATM Menu")
#     print("1. Check Balance")
#     print("2. Withdraw Money")
#     print("3. Deposit Money")
#     print("4. View Transaction History")
#     print("5. Exit")

# # Function to authenticate user using iris
# def authenticate_iris(image_path):
#     # Use argparse for image input
#     image1 = cv2.imread(image_path)

#     if image1 is None:
#         print("Error: Image could not be loaded. Check file path.")
#         exit(1)

#     # Encode the iris codes
#     code1, mask1 = encode_photo(image1)

#     # Assuming the second image is a pre-stored image for matching
#     # Replace this path with a fixed path to the stored reference image
#     stored_image_path = 'splash-eye.jpg'  
#     stored_image = cv2.imread(stored_image_path)

#     if stored_image is None:
#         print("Error: Stored reference image could not be loaded. Check file path.")
#         exit(1)

#     code2, mask2 = encode_photo(stored_image)

#     # Compare the codes and authenticate user
#     if compare_codes(code1, code2, mask1, mask2) == 0:
#         print("Iris Matched")
#         return True
#     else:
#         print("No match found")
#         return False

# def main():
#     # ATM setup
#     atm = ATM(1000)  # Initial balance is $1000

#     # Verify the PIN before iris authentication
#     if atm.verify_pin():  # Ask for PIN verification before showing the options
#         # Iris authentication
#         image_path = input("Enter path to your iris image for verification: ")
#         if not authenticate_iris(image_path):  # Authenticate using the iris image
#             print("Authentication failed. Exiting...")
#             return

#         # Proceed with ATM menu after successful PIN and iris verification
#         while True:
#             atm_menu()
#             choice = input("\nSelect an option: ")

#             if choice == '1':
#                 atm.show_balance()
#             elif choice == '2':
#                 amount = float(input("Enter the amount to withdraw: $"))
#                 atm.withdraw(amount)
#             elif choice == '3':
#                 amount = float(input("Enter the amount to deposit: $"))
#                 atm.deposit(amount)
#             elif choice == '4':
#                 atm.print_transaction_history()
#             elif choice == '5':
#                 print("Thank you for using the ATM. Goodbye!")
#                 break
#             else:
#                 print("Invalid option, please try again.")

#             time.sleep(1)  # Adding a small delay for user experience
#     else:
#         print("Exiting the ATM.")

# if __name__ == '__main__':
#     main()


import cv2
import time
from segmentation import *
from coding import *
from recognition import *

# Function to compare iris codes
def compare_codes(a, b, mask_a, mask_b, rotation=False):
    if rotation:
        d = []
        for i in range(-rotation, rotation + 1):
            c = np.roll(b, i, axis=1)
            mask_c = np.roll(mask_b, i, axis=1)
            d.append(np.sum(np.remainder(a + c, 2) * mask_a * mask_c) / np.sum(mask_a * mask_c))
        return np.min(d)
    return np.sum(np.remainder(a + b, 2) * mask_a * mask_b) / np.sum(mask_a * mask_b)

# Function to encode the iris photo
def encode_photo(image):
    img = preprocess(image)
    x, y, r = find_pupil_hough(img)
    x_iris, y_iris, r_iris = find_iris_hough(img)
    iris = unravel_iris(image, x, y, r, x_iris, y_iris, r_iris)
    return iris_encode(iris)

# ATM Class
class ATM:
    def __init__(self, balance=0, pin="1234"):
        self.balance = balance
        self.transaction_history = []
        self.pin = pin  # Default pin is set to 1234 for simplicity

    def verify_pin(self):
        # Loop to verify the PIN. The user gets 3 attempts.
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your PIN: ")
            if entered_pin == self.pin:
                print("PIN verified successfully!")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. You have {attempts} attempts remaining.")
                if attempts == 0:
                    print("No attempts remaining. Exiting...")
                    return False
        return False

    def show_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid amount to withdraw.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"Successfully withdrew ${amount}.")
            self.show_balance()

    def deposit(self, amount):
        if amount <= 0:
            print("Please enter a valid amount to deposit.")
        else:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print(f"Successfully deposited ${amount}.")
            self.show_balance()

    def print_transaction_history(self):
        print("\nTransaction History:")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for transaction in self.transaction_history:
                print(transaction)

# Function to show the ATM menu
def atm_menu():
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. View Transaction History")
    print("5. Exit")

# Function to authenticate user using iris
def authenticate_iris(image):
    # Encode the iris codes
    code1, mask1 = encode_photo(image)

    # Assuming the second image is a pre-stored image for matching
    # Replace this path with a fixed path to the stored reference image
    stored_image_path = 'splash-eye.jpg'  
    stored_image = cv2.imread(stored_image_path)

    if stored_image is None:
        print("Error: Stored reference image could not be loaded. Check file path.")
        exit(1)

    code2, mask2 = encode_photo(stored_image)

    # Compare the codes and authenticate user
    if compare_codes(code1, code2, mask1, mask2) == 0:
        print("Iris Matched")
        return True
    else:
        print("No match found")
        return False

# Function to capture iris image using webcam
def capture_iris_image():
    cap = cv2.VideoCapture(0)  # 0 is the default camera ID
    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return None

    print("Please position your face in front of the camera for iris capture.")
    time.sleep(2)  # Allow time for positioning

    # Capture a frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        cap.release()
        return None

    cap.release()  # Release the camera
    print("Image captured successfully.")
    
    # Display the captured image
    cv2.imshow('Captured Image', frame)
    cv2.waitKey(0)  # Wait for any key press to close
    cv2.destroyAllWindows()

    return frame  # Return the captured image

def main():
    # ATM setup
    atm = ATM(1000)  # Initial balance is $1000

    # Verify the PIN before iris authentication
    if atm.verify_pin():  # Ask for PIN verification before showing the options
        # Iris authentication using live camera capture
        iris_image = capture_iris_image()
        if iris_image is None:
            print("Authentication failed. Exiting...")
            return

        # Authenticate the iris image
        if not authenticate_iris(iris_image):
            print("Authentication failed. Exiting...")
            return

        # Proceed with ATM menu after successful PIN and iris verification
        while True:
            atm_menu()
            choice = input("\nSelect an option: ")

            if choice == '1':
                atm.show_balance()
            elif choice == '2':
                amount = float(input("Enter the amount to withdraw: $"))
                atm.withdraw(amount)
            elif choice == '3':
                amount = float(input("Enter the amount to deposit: $"))
                atm.deposit(amount)
            elif choice == '4':
                atm.print_transaction_history()
            elif choice == '5':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option, please try again.")

            time.sleep(1)  # Adding a small delay for user experience
    else:
        print("Exiting the ATM.")

if __name__ == '__main__':
    main()
