# This makefile acts as an execution script to backup and upload web files.
# Note: This will only work if executed from my workstation.

.PHONY: all chperm sync-drobo sync-drobo-dry sync-takeda sync-takeda-dry dry

# Shell and commands
SHELL = /bin/sh
CHMOD = /bin/chmod
FIND = /usr/bin/find
RSYNC = /usr/bin/rsync

# Directories where things reside
WPATH = "/Users/santa/Documents/proj/engineered"
UTILD = "$(WPATH)/util"
EXCLF = "$(UTILD)/rsync.exclude"
LOGF = "$(UTILD)/rsync.log"
RPATH = "rsync://droboshare/doc/proj/engineered"
TKPATH = "santa@takeda.tk:~/proj/engineered"
#TAKEDAEXCL = "peachy/*"

# Flags
RSYNCFLAGS = --recursive --links --perms --times \
             --compress --exclude-from=$(EXCLF) \
             --exclude="*.log"--log-file=$(LOGF)
RSYNCVERB = --verbose --human-readable --progress


all: sync-drobo sync-takeda

dry: sync-drobo-dry sync-takeda-dry

# change permissions
# public directories have 'rwxr-xr-x"
# public files have "rwxr--r--"
# except util/ and util/*
chperm:
	@echo "Changing permissions ..."
	@$(FIND) $(WPATH) -type d -not -regex ".*/\.git.*" -print | \
	                          xargs $(CHMOD) u=rwx,og=rx
	@$(FIND) $(WPATH) -type f -not -regex ".*/\.DS_Store" \
	                          -not -regex ".*/\.git.*" -print | \
			   	              xargs $(CHMOD) u=rw,og=r
	@$(CHMOD) u+x $(WPATH)/manage.py
	@$(CHMOD) uo+w $(WPATH)
	@$(CHMOD) uo+w $(WPATH)/comics/media/strips
	@$(CHMOD) u=rwx,og-rwx $(UTILD)
	@$(CHMOD) u-x,og-rwx $(UTILD)/*

# sync engineered/ as a backup archive over rsync to the drobo storage
sync-drobo: chperm
	@echo "Syncing to Drobo ..."
	@$(RSYNC) $(RSYNCFLAGS) $(WPATH)/ $(RPATH)
	@echo "Done."

sync-drobo-dry: chperm
	@echo "Syncing to Drobo ... (dry run)"
	@$(RSYNC) --dry-run $(RSYNCVERB) $(RSYNCFLAGS) $(WPATH)/ $(RPATH)

# sync www/ as an upload operation to takeda server
sync-takeda: chperm
	@echo "Syncing to takeda ..."
	@$(RSYNC) --update $(RSYNCFLAGS) $(WPATH)/ $(TKPATH)
	@$(RSYNC) --update $(RSYNCFLAGS) $(WPATH)/comics/media/ \
			santa@takeda.tk:~/public_html/static/engineered
	@echo "Done."

sync-takeda-dry: chperm
	@echo "Syncing to takeda ... (dry run)"
	@$(RSYNC) --update --dry-run \
			  $(RSYNCVERB) $(RSYNCFLAGS) $(WPATH)/ $(TKPATH)
	@$(RSYNC) --update --dry-run \
			$(RSYNCFLAGS) $(WPATH)/comics/media/css/ \
			santa@takeda.tk:~/public_html/static/engineered/css
