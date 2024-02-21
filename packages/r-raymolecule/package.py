# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaymolecule(RPackage):
	"""Parse and Render Molecular Structures in 3D

	Downloads and parses 'SDF' (Structural Description Format) and 'PDB' (Protein Database) files for 3D rendering.
	"""
	
	cran = "raymolecule" 

	version("0.5.0", md5="8d14be9b8ca64ab238fc587bbaddf4cc")

	depends_on("r-rayrender", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-periodictable", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rayvertex", type=("build", "run"))
