# Week 2 Lab: Linux and command-line foundations

[← Practical labs](README.md) · [← Week 2 guide](../weeks/week-02.md)

## Mission
Navigate a project directory, inspect files, filter command output, understand permissions and processes, and produce a reproducible terminal log.

**Time:** 60–90 minutes · **Cost:** Free · **Shell:** Bash

## Prerequisites
A Linux terminal, macOS Terminal, or WSL. On Windows without WSL, use a Linux lab machine or Cloud Shell only if the facilitator has approved it. Do not run unfamiliar commands with `sudo`.

## Part A — Identify your environment

Run:

```bash
whoami
pwd
uname -a
printf 'Shell: %s\n' "$SHELL"
```

Expected: your local username, current directory, operating-system/kernel information and shell path. Exact values vary.

**Explain:** What does `pwd` show? Why is the username useful when diagnosing file-permission errors?

## Part B — Create a safe workspace

```bash
mkdir -p ~/cloud-track/week-02/{input,output}
cd ~/cloud-track/week-02
printf 'cloud\nlinux\nengineering\ncloud\n' > input/topics.txt
printf 'week=02\nstatus=started\n' > input/session.env.example
find . -maxdepth 2 -type f -print
```

Expected files:
- `input/topics.txt`
- `input/session.env.example`

The file is deliberately named `.env.example`; never put real credentials in it.

## Part C — Read and transform data

```bash
cat input/topics.txt
wc -l input/topics.txt
sort input/topics.txt
sort input/topics.txt | uniq -c
grep -n 'cloud' input/topics.txt
```

Expected observations:
- `wc -l` reports 4 lines.
- `sort` orders the words.
- `uniq -c` shows the repeated word with count 2.
- `grep` returns the two lines containing cloud.

Save a sorted copy:

```bash
sort input/topics.txt | uniq > output/unique-topics.txt
cat output/unique-topics.txt
```

**Explain:** What does the pipe (`|`) do? Why does `uniq` usually need sorted input to find all duplicates?

## Part D — Understand permissions

```bash
ls -l input
chmod 600 input/session.env.example
stat -c '%A %a %n' input/session.env.example 2>/dev/null || ls -l input/session.env.example
```

Expected: the example file is readable and writable only by its owner on typical Unix permissions. The `stat` format differs on macOS; the fallback `ls` command works there.

Restore ordinary read access for your own learning file if desired:

```bash
chmod 644 input/session.env.example
```

Never use `chmod -R 777` as a generic fix. It grants broad permissions and can expose sensitive files.

## Part E — Inspect processes

```bash
ps
ps aux | head
```

Expected: a process listing. Your exact process list will differ.

Start a short-lived process and find it:

```bash
sleep 300 &
echo $!
ps -p $! -o pid,comm
```

Stop only the process you started:

```bash
kill $!
```

Confirm it has exited:

```bash
ps -p $! -o pid,comm
```

No output is a normal result after the process exits. Avoid broad commands such as `killall` during this exercise.

## Part F — Environment variables

```bash
export CLOUD_TRACK_WEEK=02
printf '%s\n' "$CLOUD_TRACK_WEEK"
```

Expected output: `02`. The variable exists in the current shell session; it is not automatically saved for future terminals.

## Core challenge
Write a script named `output/inspect-workspace.sh` that:
1. Prints the current directory.
2. Counts lines in `input/topics.txt`.
3. Prints unique topics.
4. Exits with a non-zero status if the input file is missing.

Starter:

```bash
#!/usr/bin/env bash
set -euo pipefail

# TODO: check that input/topics.txt exists
# TODO: print the working directory
# TODO: count lines
# TODO: print unique topics
```

Make it executable and run it:

```bash
chmod +x output/inspect-workspace.sh
./output/inspect-workspace.sh
```

## Intermediate stretch
Use `awk` to count occurrences of each topic, then explain the difference between `grep`, `sort`, `uniq` and `awk`. Add a command that writes a timestamped run log without overwriting earlier logs.

## Troubleshooting
- **Permission denied:** inspect `ls -l`, confirm you own the file, and check whether the script has execute permission. Do not immediately use `sudo`.
- **Command not found:** record your OS and shell; install tools only from trusted package repositories or use an approved lab environment.
- **No process shown:** it may have exited before inspection. Start it again and inspect promptly.
- **Different `stat` output:** use the `ls -l` fallback; options differ between GNU and BSD/macOS tools.

## Evidence
Submit a sanitized `week-02-evidence.md` with environment (OS/shell), key commands and outputs, your script, one permission explanation, one pipeline explanation and one issue you resolved. Never include private paths or usernames if you do not want them public.

## Cleanup
From the lab directory, inspect before removing:

```bash
find ~/cloud-track/week-02 -maxdepth 3 -type f -print
```

Keep the folder as evidence or remove only this exercise directory when finished:

```bash
rm -r ~/cloud-track/week-02
```

Read the path carefully before pressing Enter.
