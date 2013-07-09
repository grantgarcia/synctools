from inspect import isclass

from synctools.commands import *
import synctools.commands

all_commands = []
for module in [locals()[module] for module in synctools.commands.__all__]:
    for attr in module.__dict__.values():
        if isclass(attr) and issubclass(attr, synctools.commands.SynctoolsCommand):
            all_commands.append(attr)