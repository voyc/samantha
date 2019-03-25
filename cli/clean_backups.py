import glob, os, os.path
from os.path import isfile, join
import shutil

total, used, free = shutil.disk_usage("/home/jhagstrand/db_backups")

print(total)
print(used)
print(free)

print("Total: %d GB" % (total // (2**30)))
print("Used: %d GB" % (used // (2**30)))
print("Free: %d GB" % (free // (2**30)))

# move keepers to archive
dstdir = "/home/jhagstrand/backup_archive/"
srcdir = "/home/jhagstrand/db_backups/"
mask = "*.??????01.*"
src = join(srcdir, mask)
for f in glob.glob(src):
	shutil.move(f, dstdir)

# delete everything else
src = join(srcdir, "*.sql")
for f in glob.glob(src):
	os.remove( f)
