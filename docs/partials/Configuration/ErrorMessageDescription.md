The message can be separated in 3 parts

???+ info "The Logs"
    ```
    2023/01/20 - 14:59:09 ERROR    Key storage_account_name can not be found in platform config file
    2023/01/20 - 14:59:09 ERROR    storage won't run without it.
    ```

??? failure "The Trace"
    ```
    ╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────────╮
    │ /home/afossart/git_repos/Babylon/.venv/bin/babylon:11 in <module>                                    │
    │                                                                                                      │
    │    8 if __name__ == '__main__':                                                                      │
    │    9 │   sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])                           │
    │   10 │   sys.exit(                                                                                   │
    │ ❱ 11 │   │   load_entry_point('Babylon', 'console_scripts', 'babylon')()                             │
    │   12 │   )                                                                                           │
    │   13                                                                                                 │
    │                                                                                                      │
    │ /home/afossart/git_repos/Babylon/.venv/lib/python3.9/site-packages/click/core.py:1130 in __call__    │
    │                                                                                                      │
    │   1127 │                                                                                             │
    │   1128 │   def __call__(self, *args: t.Any, **kwargs: t.Any) -> t.Any:                               │
    │   1129 │   │   """Alias for :meth:`main`."""                                                         │
    │ ❱ 1130 │   │   return self.main(*args, **kwargs)                                                     │
    │   1131                                                                                               │
    │   1132                                                                                               │
    │   1133 class Command(BaseCommand):                                                                   │
    │                                                                                                      │
    │ /home/afossart/git_repos/Babylon/.venv/lib/python3.9/site-packages/click/core.py:1055 in main        │
    │                                                                                                      │
    │   1052 │   │   try:                                                                                  │
    │   1053 │   │   │   try:                                                                              │
    │   1054 │   │   │   │   with self.make_context(prog_name, args, **extra) as ctx:                      │
    │ ❱ 1055 │   │   │   │   │   rv = self.invoke(ctx)                                                     │
    │   1056 │   │   │   │   │   if not standalone_mode:                                                   │
    │   1057 │   │   │   │   │   │   return rv                                                             │
    │   1058 │   │   │   │   │   # it's not safe to `ctx.exit(rv)` here!                                   │
    │                                                                                                      │
    │ /home/afossart/git_repos/Babylon/.venv/lib/python3.9/site-packages/click/core.py:1657 in invoke      │
    │                                                                                                      │
    │   1654 │   │   │   │   super().invoke(ctx)                                                           │
    │   1655 │   │   │   │   sub_ctx = cmd.make_context(cmd_name, args, parent=ctx)                        │
    │   1656 │   │   │   │   with sub_ctx:                                                                 │
    │ ❱ 1657 │   │   │   │   │   return _process_result(sub_ctx.command.invoke(sub_ctx))                   │
    │   1658 │   │                                                                                         │
    │   1659 │   │   # In chain mode we create the contexts step by step, but after the                    │
    │   1660 │   │   # base command has been invoked.  Because at that point we do not                     │
    │                                                                                                      │
    │ /home/afossart/git_repos/Babylon/.venv/lib/python3.9/site-packages/click/core.py:1657 in invoke      │
    │                                                                                                      │
    │   1654 │   │   │   │   super().invoke(ctx)                                                           │
    │   1655 │   │   │   │   sub_ctx = cmd.make_context(cmd_name, args, parent=ctx)                        │
    │   1656 │   │   │   │   with sub_ctx:                                                                 │
    │ ❱ 1657 │   │   │   │   │   return _process_result(sub_ctx.command.invoke(sub_ctx))                   │
    │   1658 │   │                                                                                         │
    │   1659 │   │   # In chain mode we create the contexts step by step, but after the                    │
    │   1660 │   │   # base command has been invoked.  Because at that point we do not                     │
    │                                                                                                      │
    │ /home/afossart/git_repos/Babylon/.venv/lib/python3.9/site-packages/click/core.py:1654 in invoke      │
    │                                                                                                      │
    │   1651 │   │   │   │   cmd_name, cmd, args = self.resolve_command(ctx, args)                         │
    │   1652 │   │   │   │   assert cmd is not None                                                        │
    │   1653 │   │   │   │   ctx.invoked_subcommand = cmd_name                                             │
    │ ❱ 1654 │   │   │   │   super().invoke(ctx)                                                           │
    │   1655 │   │   │   │   sub_ctx = cmd.make_context(cmd_name, args, parent=ctx)                        │
    │   1656 │   │   │   │   with sub_ctx:                                                                 │
    │   1657 │   │   │   │   │   return _process_result(sub_ctx.command.invoke(sub_ctx))                   │
    │                                                                                                      │
    │ /home/afossart/git_repos/Babylon/.venv/lib/python3.9/site-packages/click/core.py:1404 in invoke      │
    │                                                                                                      │
    │   1401 │   │   │   echo(style(message, fg="red"), err=True)                                          │
    │   1402 │   │                                                                                         │
    │   1403 │   │   if self.callback is not None:                                                         │
    │ ❱ 1404 │   │   │   return ctx.invoke(self.callback, **ctx.params)                                    │
    │   1405 │                                                                                             │
    │   1406 │   def shell_complete(self, ctx: Context, incomplete: str) -> t.List["CompletionItem"]:      │
    │   1407 │   │   """Return a list of completions for the incomplete value. Looks                       │
    │                                                                                                      │
    │ /home/afossart/git_repos/Babylon/.venv/lib/python3.9/site-packages/click/core.py:760 in invoke       │
    │                                                                                                      │
    │    757 │   │                                                                                         │
    │    758 │   │   with augment_usage_errors(__self):                                                    │
    │    759 │   │   │   with ctx:                                                                         │
    │ ❱  760 │   │   │   │   return __callback(*args, **kwargs)                                            │
    │    761 │                                                                                             │
    │    762 │   def forward(                                                                              │
    │    763 │   │   __self, __cmd: "Command", *args: t.Any, **kwargs: t.Any  # noqa: B902                 │
    │                                                                                                      │
    │ /home/afossart/git_repos/Babylon/.venv/lib/python3.9/site-packages/click/decorators.py:26 in new_func│
    │                                                                                                      │
    │    23 │   """                                                                                        │
    │    24 │                                                                                              │
    │    25 │   def new_func(*args, **kwargs):  # type: ignore                                             │
    │ ❱  26 │   │   return f(get_current_context(), *args, **kwargs)                                       │
    │    27 │                                                                                              │
    │    28 │   return update_wrapper(t.cast(F, new_func), f)                                              │
    │    29                                                                                                │
    │                                                                                                      │
    │ /home/afossart/git_repos/Babylon/Babylon/utils/decorators.py:209 in wrapper                          │
    │                                                                                                      │
    │   206 │   │   │   │   if value in [None, ""] and required:                                           │
    │   207 │   │   │   │   │   logger.error(f"Key {yaml_key} can not be found in {getter.__doc__}")       │
    │   208 │   │   │   │   │   logger.error(f"{click.get_current_context().command.name} won't run        │
    │ ❱ 209 │   │   │   │   │   raise KeyError(f"Key {yaml_key} can not be found in {getter.__doc__}       │
    │   210 │   │   │   │   return func(*args, **kwargs)                                                   │
    │   211 │   │   │                                                                                      │
    │   212 │   │   │   if not required:                                                                   │
    ╰──────────────────────────────────────────────────────────────────────────────────────────────────────╯
    ```

??? warning "The Error"
    ```
    KeyError: 'Key storage_account_name can not be found in platform config file'
    ```

In most cases, you can focus on the logs at the beginning of the message, 
if this is a known error it should give you enough information on how to solve it.  
Here we can see that the key `storage_account_name` is not found in the `platform config file` and that the command will not run without it.

In case the logs are not enough you can look at the error, which should help you, and if neither helps you can start an issue on the Babylon repository by sending the command you ran and the trace.