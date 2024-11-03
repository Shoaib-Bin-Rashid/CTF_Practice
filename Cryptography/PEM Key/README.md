# PEM Key Management

This directory contains PEM (Privacy-Enhanced Mail) formatted keys and certificates used in various cryptographic applications.

## Table of Contents

- [What is a PEM Key?](#what-is-a-pem-key)
- [Common PEM File Types](#common-pem-file-types)
- [PEM Key Structure](#pem-key-structure)
- [How to Read a PEM Key](#how-to-read-a-pem-key)
- [Common Commands](#common-commands)
- [Resources](#resources)

## What is a PEM Key?

PEM (Privacy-Enhanced Mail) is a widely used file format for storing and sharing cryptographic keys and certificates. PEM files are ASCII-encoded and include headers and footers that indicate the type of content they contain, such as private keys, public keys, or certificates.

## Common PEM File Types

- **Private Key**: Stores the private part of a key pair, often used in asymmetric cryptography.
- **Public Key**: Contains the public part of a key pair, which can be shared publicly.
- **Certificate**: A digital certificate that binds a public key to an identity.

## PEM Key Structure

A typical PEM file has the following format:
-----BEGIN [TYPE]----- [Base64 Encoded Data] -----END [TYPE]-----


Where `[TYPE]` could be one of the following:
- `RSA PRIVATE KEY`
- `PUBLIC KEY`
- `CERTIFICATE`

## How to Read a PEM Key

You can read and decode PEM keys using various methods:

### Using OpenSSL

To read a PEM file, you can use the OpenSSL command-line tool. Here are some examples:

1. **To read a private key**:
   ```bash
   openssl rsa -in your_key.pem -text -noout
2.**To read a public key**:
  ```bash
  openssl rsa -pubin -in your_public_key.pem -text -noout
3.To read a certificate:
  ```bash
  openssl x509 -in your_certificate.pem -text -noout
