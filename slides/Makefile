HTML_FILES := $(patsubst %.Rmd, %.html ,$(wildcard *.Rmd)) \
              $(patsubst %.md, %.html, $(wildcard *.md))

HTML_DIR := $(patsubst %.Rmd, %_files , $(wildcard *.Rmd)) \
            $(patsubst %.md, %_files, $(wildcard *.md))

all: clean html removedir

html: $(HTML_FILES)

%.html: %.Rmd
	R --slave -e "set.seed(100);rmarkdown::render('$<')"

%.html: %.md
	R --slave -e "set.seed(100);rmarkdown::render('$<')"

.PHONY: clean removedir
clean:
	$(RM) $(HTML_FILES)
removedir:
	$(RM) -r $(HTML_DIR)

