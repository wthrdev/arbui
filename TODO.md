
### Commands to add
Always use --json in parameters for parsing data.

#### High priority

- [ ] `restic init --repository {PATH}` — Use $RESTIC_PASSWORD for setting
- [ ] `restic snapshots` 
    - [ ] `-c` / `--compact`
    - [ ] `--path {PATH}`

- [ ] `restic forget` 
- [ ] `restic backup {PATH} ` (`--tag {TAG}`) (`--compression [off/auto/max]`)
- [ ] `restic restore ` (`--overwrite {always/never})
- [ ] `restic ls`

#### TBA later...

- [ ] `restic repair`
- [ ] `restic recover`
- [ ] `restic copy`
- [ ] `restic check`
- [ ] `restic diff`
