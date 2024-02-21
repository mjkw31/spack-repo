# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasiliskUtils(RPackage):
	"""Basilisk Installation Utilities.

	Implements utilities for installation of the basilisk package, primarily
	for creation of the underlying Conda instance. This allows us to avoid
	re-writing the same R code in both the configure script (for centrally
	administered R installations) and in the lazy installation mechanism (for
	distributed package binaries). It is highly unlikely that developers - or,
	heaven forbid, end-users! - will need to interact with this package
	directly; they should be using the basilisk package instead."""

	bioc = "basilisk.utils"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/basilisk.utils_1.14.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/basilisk.utils/basilisk.utils_1.14.1.tar.gz"]

	version("1.14.1", md5="d5e61359283886e8653f772e65b0a898")

	depends_on("r-dir-expiry", type=("build", "run"))
