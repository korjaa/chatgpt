TOOLS := ${HOME}/.shortcuts/ChatGPT
TOOLS += ${HOME}/.shortcuts/CarGPT

.PHONY: default
default:
	echo "make install"

${HOME}/.shortcuts:
	mkdir "$@"

${HOME}/.shortcuts/ChatGPT: | ${HOME}/.shortcuts
	cp chatgpt.sh "$@"

${HOME}/.shortcuts/CarGPT: | ${HOME}/.shortcuts
	cp cargpt.sh "$@"

.PHONY: install
install: ${TOOLS}

.PHONY: uninstall
uninstall:
	rm -rf ${TOOLS}
