
# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install r-vdiffr
#
# You can edit this file again by typing:
#
#     spack edit r-vdiffr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RVdiffr(RPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://vdiffr.r-lib.org/"
    cran = "vdiffr"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    version("1.0.6", sha256="620194676791fbbb303ea998d12544017d97c4ee975fed1e416ae99de74d23d6")

    # FIXME: Add dependencies if required.
    depends_on("r-diffobj", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-lifecycle", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
    depends_on("libpng", type=("build", "link"))
    depends_on("r-cpp11", type=("build", "run"))

