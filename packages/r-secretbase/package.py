# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSecretbase(RPackage):
	"""Cryptographic Hash and Extendable-Output Functions

	SHA-3 cryptographic hash and SHAKE256 extendable-output functions
    (XOF). The SHA-3 Secure Hash Standard was published by the National
    Institute of Standards and Technology (NIST) in 2015 at
    <doi:10.6028/NIST.FIPS.202>. Fast and memory-efficient implementation using
    the core algorithm from 'Mbed TLS' under the Trusted Firmware Project
    <https://www.trustedfirmware.org/projects/mbed-tls/>.
	"""
	
	homepage = "https://shikokuchuo.net/secretbase/"
	cran = "secretbase" 

	version("0.2.0", md5="abb9f4901ce67b64aa31d298166b9a4b")

	depends_on("r@3.5:", type=("build", "run"))
