import key, auth
from encodex import encode, decode

def main():
    choice = input("LogIn/SignIn: ").strip().lower()
    if choice == "login":
        success, seed = auth.login()
        if success:
            choice = input("Encode/Decode: ").strip().lower()
            if choice == "encode":
                print(encode(seed))
            elif choice == "decode":
                print(decode(seed))
            else: 
                print("Invalid.")
        else:
            print("Invalid.")
    elif choice == "signin":
        generated_seed =key.key_generator()
        print(generated_seed)
    else:
        print("Invalid.")


if __name__ == "__main__":
    main()