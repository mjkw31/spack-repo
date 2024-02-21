# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnc(RPackage):
	"""Portable Tools for 'UTF-8' Character Data

	
    Implements an S3 class for storing 'UTF-8' strings, based on regular character vectors.
    Also contains routines to portably read and write 'UTF-8' encoded text files,
    to convert all strings in an object to 'UTF-8',
    and to create character vectors with various encodings.
	"""
	
	homepage = "https://github.com/krlmlr/enc"
	cran = "enc" 

	version("0.2.2", md5="1b7a49659d430e92493a5ca892d99643")

	depends_on("r@3.1:", type=("build", "run"))
