CLOSURE := \
	closure-compiler

CLOSUREOPTS := \
	 --compilation_level=SIMPLE \
	 --language_in=ECMASCRIPT5_STRICT

js_app_targets := \
	app.js app-min.js

js_app_sources := \
	$(wildcard src/js/*.js)

html_sources := \
	$(wildcard src/js/*.js)

assets := \
	$(wildcard assets/*) \
	$(wildcard 3rd-party/assets/*)

css_sources := \
	$(wildcard src/css/*.css) \
	$(wildcard 3rd-party/css/*.css)

js_extra_sources := \
	$(wildcard 3rd-party/js/*.js)

statics := \
	$(assets) \
	$(css_sources) \
	$(js_extra_sources)

# NB: Preserve directory hierarchy for HTML sources. For all other stuff
# ignore the hierarchy and just put them under /s/.
targets := \
	$(patsubst src/html/%, build/dist/%, $(html_sources)) \
	$(addprefix build/dist/s/, $(js_app_targets)) \
	$(addprefix build/dist/s/, $(notdir $(statics)))

.PHONY: all
all: $(targets)

# NB: Don't do this while the server is running. Currently this will crash the
# server.
.PHONY: clean
clean:
	rm -rf build

# Guaranteed to fail
.PHONY: bomb
build/dist/bomb.html:
	false

# Copy HTML as-is
build/dist/%.html: src/html/%.html
	@test -e $(@D) || mkdir -p $(@D)
	cp $< $@

# Fold all our own JS into an app
build/dist/s/app.js: $(js_app_sources)
	@test -e $(@D) || mkdir -p $(@D)
	cat $^ > $@

# Copy our own CSS as-is
build/dist/s/%.css: src/css/%.css
	@test -e $(@D) || mkdir -p $(@D)
	cp $< $@

# Copy 3rd-party JS as-is
build/dist/s/%.js: 3rd-party/js/%.js
	@test -e $(@D) || mkdir -p $(@D)
	cp $< $@

# Copy 3rd-party assets as-is
build/dist/s/%: 3rd-party/assets/%
	@test -e $(@D) || mkdir -p $(@D)
	cp $< $@

# Minify (anything and not just app.js)
build/%-min.js: build/%.js
	@test -e $(@D) || mkdir -p $(@D)
	$(CLOSURE) $(CLOSUREOPTS) --js=$< --js_output_file=$@

# Dynamically generate a .png containing the corresponding QR code
build/dist/qr/%.png:
	@test -e $(@D) || mkdir -p $(@D)
	qr "$@" > "$@"
