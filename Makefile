
TOOLS := ${HOME}/bin/chatgpt
TOOLS += ${HOME}/bin/cargpt

.PHONY: default
default:
	echo "make install"

${HOME}/bin:
	mkdir "$@"

venv:
	virtualenv venv
	venv/bin/python -m pip install -e .

${HOME}/bin/chatgpt: | ${HOME}/bin venv
	ln -s "$(shell pwd)/venv/bin/chatgpt" "$@"

${HOME}/bin/cargpt: | ${HOME}/bin venv
	ln -s "$(shell pwd)/venv/bin/cargpt" "$@"

${HOME}/bin/pythongpt: | ${HOME}/bin venv
	ln -s "$(shell pwd)/venv/bin/pythongpt" "$@"

.PHONY: install
install: ${TOOLS}

.PHONY: uninstall
uninstall:
	rm -rf ${TOOLS}
