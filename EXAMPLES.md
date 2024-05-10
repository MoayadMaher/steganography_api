### hide:

```
To hide a file within an image, use the following commands:
- `python generate_keys.py`
    - This command generates a pair of RSA keys: a private key and a public key.

- `python secret_pixel.py hide images/example.png secret.txt public.pub images/example_secret.png`
    - This command embeds `secret.txt` inside `images/example.png` using the public key `public.pub`, and saves the steganographed image as `images/example_secret.png`.
```

## extract:

```
python secret_pixel.py extract images/example_secret.png private.pem images/secret_png.txt
```
