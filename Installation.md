## 📥 Installation

pip install the library:

```sh
pip install cryptmoji
```

## 📝 Usage

```python
from cryptmoji import Cryptmoji
text = "Hello World!"
key = "random_key" # makes the encryption stronger (optional)
a = Cryptmoji(text, key=key)
# The encrypt and decrypt functions return the value
encrypted = a.encrypt()
print(encrypted)
# 🎚️🎨🎼🎲🏀🍯🎓🎼🎹🏂🎸🍤
# The encrypt and decrypt functions change the value in-place too
a.decrypt()
print(decrypted)
# Hello World!
```

#### Created and Managed by [Siddhesh Agarwal](https://github.com/Siddhesh-Agarwal/cryptmoji)
