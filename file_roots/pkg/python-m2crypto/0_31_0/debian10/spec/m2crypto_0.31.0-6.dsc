-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Format: 3.0 (quilt)
Source: m2crypto
Binary: python-m2crypto, python3-m2crypto, m2crypto-doc
Architecture: any all
Version: 0.31.0-6
Maintainer: Daniel Stender <stender@debian.org>
Uploaders: Debian Python Modules Team <python-modules-team@lists.alioth.debian.org>
Homepage: https://gitlab.com/m2crypto/m2crypto
Standards-Version: 4.4.0
Vcs-Browser: https://salsa.debian.org/python-team/modules/m2crypto
Vcs-Git: https://salsa.debian.org/python-team/modules/m2crypto.git
Testsuite: autopkgtest
Testsuite-Triggers: openssl, python-pytest
Build-Depends: debhelper-compat (= 12), dh-python, libssl-dev, python-all-dev, python3-all-dev, python-setuptools, python3-setuptools, swig (>= 1.3.40), python-pytest <!nocheck>, python3-pytest <!nocheck>, python-typing <!nocheck>, openssl <!nocheck>, python-docutils <!nodoc>, links <!nodoc>, python3-sphinx <!nodoc>
Package-List:
 m2crypto-doc deb doc optional arch=all profile=!nodoc
 python-m2crypto deb python optional arch=any
 python3-m2crypto deb python optional arch=any
Checksums-Sha1:
 0ada6dd60c66c3ec8d7497c2ffa6fb1ad08f46a7 892799 m2crypto_0.31.0.orig.tar.gz
 5be8141620a03035073cb1eca40738ed0540faf0 59716 m2crypto_0.31.0-6.debian.tar.xz
Checksums-Sha256:
 5d14d4b59c270d2e43ad3e24e855deb3e9f52544be83d9df1ff9417c06c13985 892799 m2crypto_0.31.0.orig.tar.gz
 89699cc56d0f7fb1a127dac26373e932ae11f9b08e439ca4ae8c711e5fad6651 59716 m2crypto_0.31.0-6.debian.tar.xz
Files:
 bcf42b36e2eccf5d0254ed7c94d5fb31 892799 m2crypto_0.31.0.orig.tar.gz
 75327a52d83f56bacf0cc04c60d24776 59716 m2crypto_0.31.0-6.debian.tar.xz

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCgAdFiEERsscqJ6jt0N2dh25FeCa9N9RgsgFAl1Zf7EACgkQFeCa9N9R
gsjrjg/+JX1uvjg4l4NE+6UoUXFGXL3cUh/ilQdo7tHdqj/FO4GYkQTh8DO/1KRE
MgAwyWccKMo4JrMMPIwrmabqKPeifI6CwaO0c7vS9yVYdUtztKCiUdmIl8PW50mZ
KvQCRqii6OvU+pChcoBwuaA/mCxEk/6+9z0BISV8rD7YnELjb/KRpmBKDwMUudAy
ODzLQvLGLlmw87xHX5rKkJp94t/rnP6AlPind78NfiJylncu64gMV5EPlUAe8zC6
RpVDAMCK1JPuaT3jwhUWUtiwmLCjUZZd7SrfFJWjtUfe1hxH/WfAXUwHgKyOAOEE
7MkilubHPQ4VwNEwbYgCCt2uzUAJor+oD6JsK6ugZO7aicRxQURrxRhKjvpxcQRu
TNKX2ZDUItdRMFGuLp9IThSoUXr8dEh9NSLUmO+Lxa9iCr5t5Smw8Sqza2CM5+1v
qY56C3jPC+JxbmwfTg8/RuIGG0Wmy8UzvdKw8EgfAHg2+MmX1nXegQhGe0VrFq1n
xwV5jKbFgOAve6NZs1bZpf4c15dLFbluslCuvpPBV56kp/IGmOwP5yDxSV5NEcPj
6SWlU4liQl5a0A7slMATkD8tI8EIAJc+epEYcMycxMfsy7ODSJQu9slkl0wvc2b7
UutGqhPRJRLXgrkJhIkjKuhm/5GcSlAYK0J2JFVgzDEvZCkk0aw=
=6oDM
-----END PGP SIGNATURE-----
