-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

Format: 3.0 (quilt)
Source: pyzmq
Binary: python-zmq, python-zmq-dbg, python3-zmq, python3-zmq-dbg, pypy-zmq
Architecture: any
Version: 17.1.2-2
Maintainer: Debian Python Modules Team <python-modules-team@lists.alioth.debian.org>
Uploaders: Julian Taylor <jtaylor.debian@googlemail.com>, Vincent Bernat <bernat@debian.org>, Laszlo Boszormenyi (GCS) <gcs@debian.org>
Homepage: http://www.zeromq.org/bindings:python
Standards-Version: 4.2.1
Vcs-Browser: https://salsa.debian.org/python-team/modules/pyzmq
Vcs-Git: https://salsa.debian.org/python-team/modules/pyzmq.git
Testsuite: autopkgtest
Testsuite-Triggers: pypy-pytest, python-all, python-all-dbg, python-gevent, python-gevent-dbg, python-nose, python-numpy, python-numpy-dbg, python-pytest, python-tornado, python3-all, python3-all-dbg, python3-nose, python3-numpy, python3-numpy-dbg, python3-pytest, python3-tornado
Build-Depends: cython (>= 0.20-1~), cython-dbg (>= 0.20-1~), debhelper (>= 9~), dh-python (>= 1.20131021-1~), dpkg-dev (>= 1.16.1~), libzmq3-dev, pypy (>= 2.2), pypy-pytest, python-all-dbg (>= 2.7.3-1~), python-all-dev (>= 2.7.3-1~), python-cffi, python-cffi-backend-dbg, python-gevent, python-gevent-dbg, python-nose, python-numpy, python-numpy-dbg, python-pytest, python-setuptools, python-tornado (>= 4.0), python3 (>= 3.3.0-1~), python3-all-dbg (>= 3.3.0-1~), python3-all-dev (>= 3.3.0-1~), python3-cffi, python3-cffi-backend-dbg, python3-pytest, python3-tornado (>= 4.0)
Package-List:
 pypy-zmq deb python optional arch=any
 python-zmq deb python optional arch=any
 python-zmq-dbg deb debug optional arch=any
 python3-zmq deb python optional arch=any
 python3-zmq-dbg deb debug optional arch=any
Checksums-Sha1:
 f431ad2ae1c6777c572569124d1dda27d86815d5 373668 pyzmq_17.1.2.orig.tar.gz
 22ad5b189f20153fd42a1b9904fb08f6d5da9b70 9616 pyzmq_17.1.2-2.debian.tar.xz
Checksums-Sha256:
 77a32350440e321466b1748e6063b34a8a73768b62cb674e7d799fbc654b7c45 373668 pyzmq_17.1.2.orig.tar.gz
 9d0f4e23551dd553d94477f8bb5dbb7e11e9cef79aac04ed8b4c7f1df04354bc 9616 pyzmq_17.1.2-2.debian.tar.xz
Files:
 b368115d2c5989dc45ec63a9da801df6 373668 pyzmq_17.1.2.orig.tar.gz
 135cb203686708c0acb99e0fb0dd7059 9616 pyzmq_17.1.2-2.debian.tar.xz

-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEfYh9yLp7u6e4NeO63OMQ54ZMyL8FAlxEKN0ACgkQ3OMQ54ZM
yL9taw/+NFW/8hHlrgdH/20HSV0t6pDPP20Gs8bnVIugx+leHntAasZLXLSovJs+
U7wYpX1E2WwSojiBmFTwzdfHblOgNU3qgbj+AKFKV3cChN46Bmy5NunttDgrooSq
AFSiG3oDkiUCObUQr3zq/o0lKaZ1+SXkoouAM2V/XKMvGKYPpHi6e6NJFcT07cbm
PpX+j4mm+gvQF01ZMRwGYeTpomCWNC8LuMRcU4EDOcc6yGsvYBfTCFOv1dVn3Tp0
5OQhA6vS56kVNH+l/FHA7HBEM69UarjvY0U12PFNXg5W57VoIigPJH+CjzW/J8MD
oJaifev+cCRaaqzWzzDyv+qD6XXsEWPKY07aFDKwonj9RTHL/qfk8uBLHDLHQpH9
s48hfN6arMdGenPKIsnOD/jAH8C3etJeWT4YfnT6uvy3tdznpJxKmCddYLV5qBNN
Hxrb4XtwjJoRn8BJIwEaEQCxXgs941o7nGe2kILHXVyUtrACoYs+hqId14hxDiY5
Vov/6m70rkn2EM2L806NJq+/nfBpj2Z2523FRCUsnXSl8hpn39MetCt4e9sQvMZ+
UXMpWGXlc2gUYengmaHGlF/e6YueyDLIm//JNbbQ+4jqn3vPX/kRB9IJQMV9WyUZ
svFjXQ5IxBE6noweLdxAVEpiXcbeeyaKywx1Pp0/eKS93nsWYTw=
=M09C
-----END PGP SIGNATURE-----
