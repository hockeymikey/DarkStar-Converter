# Old Name Converter

A tool that is able to converts username-based file names (of users that may have been renamed) to UUID-based file names.

# Example:

| Old filename      | New filename                                |
| :-----------      | :-----------                                |
| jomo.json         | ae795aa8-6327-408e-92ab-25c8a59f3ba1.json   |
| Djinnibutt.tar.gz | 3e50893f-4903-402f-b3b8-10158c6ed75b.tar.gz |

# Usage

`convert-old-names.py [-s] [-D] [-f] [-u] [-t timestamp] [dir]`

```txt

-s
  simulate. don't rename any files
    default: do not simulate

-D
  don't use dashed UUID format
    default: use dashed UUIDs

-f
  force overwrite existing UUID files
    default: skip existing files

-u
  use uppercase UUIDs
    default: lowercase UUIDs

-t <timestamp>
  use instead of file date
    default: uses the oldest file date (`stat`) to get the UUID for a name *at that date*.
             Please note that Linux does not store the file creation date (BSD & Windows do)

<dir>
  directory to convert files in
    default: current directory
```