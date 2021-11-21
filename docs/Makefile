# Makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
ifneq ($(shell command -v sphinx-build),)
SPHINXBUILD   ?= sphinx-build
endif
SOURCEDIR     = source
BUILDDIR      = _build

# User-friendly check for sphinx-build (if called with no arguments, exits with exit code 2)
ifneq ($(shell $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 2)
$(error "The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/")
endif

.PHONY: help clean Makefile

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	rm -rf $(BUILDDIR)/*

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
