## Example
For instance, you can run as follows:
```python
import paramiko_interactive
i = paramiko_interactive.Interactive()
hosts = ['YOUR HOST A', 'YOUR HOST B']
i.fdisk_test(hosts)
```

Then, you will get a `dict` of values like this:
```json
{
    'YOUR HOST A': ['\n', 'Welcome to fdisk (util-linux 2.30.2).\n', 'Changes will remain in memory only, until you decide to write them.\n', 'Be careful before using the write command.\n', '\n', '\n', 'Command (m for help): \n', 'Help:\n', '\n', '  Generic\n', '   d   delete a partition\n', '   F   list free unpartitioned space\n', '   l   list known partition types\n', '   n   add a new partition\n', '   p   print the partition table\n', '   t   change a partition type\n', '   v   verify the partition table\n', '   i   print information about a partition\n', '\n', '  Misc\n', '   m   print this menu\n', '   x   extra functionality (experts only)\n', '\n', '  Script\n', '   I   load disk layout from sfdisk script file\n', '   O   dump disk layout to sfdisk script file\n', '\n', '  Save & Exit\n', '   w   write table to disk and exit\n', '   q   quit without saving changes\n', '\n', '  Create a new label\n', '   g   create a new empty GPT partition table\n', '   G   create a new empty SGI (IRIX) partition table\n', '   o   create a new empty DOS partition table\n', '   s   create a new empty Sun partition table\n', '\n', '\n', 'Command (m for help): \n'], 
    'YOUR HOST B': ['\n', 'Welcome to fdisk (util-linux 2.30.2).\n', 'Changes will remain in memory only, until you decide to write them.\n', 'Be careful before using the write command.\n', '\n', '\n', 'Command (m for help): \n', 'Help:\n', '\n', '  Generic\n', '   d   delete a partition\n', '   F   list free unpartitioned space\n', '   l   list known partition types\n', '   n   add a new partition\n', '   p   print the partition table\n', '   t   change a partition type\n', '   v   verify the partition table\n', '   i   print information about a partition\n', '\n', '  Misc\n', '   m   print this menu\n', '   x   extra functionality (experts only)\n', '\n', '  Script\n', '   I   load disk layout from sfdisk script file\n', '   O   dump disk layout to sfdisk script file\n', '\n', '  Save & Exit\n', '   w   write table to disk and exit\n', '   q   quit without saving changes\n', '\n', '  Create a new label\n', '   g   create a new empty GPT partition table\n', '   G   create a new empty SGI (IRIX) partition table\n', '   o   create a new empty DOS partition table\n', '   s   create a new empty Sun partition table\n', '\n', '\n', 'Command (m for help): \n']
}
```