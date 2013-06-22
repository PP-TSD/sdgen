.PHONY: code json

generate: generate-code generate-json

clean: clean-code clean-json

generate-code:
		make -C code generate

generate-json:
		make -C json generate
		
clean-code:
		make -C code clean

clean-json:
		make -C json clean
