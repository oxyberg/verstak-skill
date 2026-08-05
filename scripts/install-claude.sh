#!/bin/sh

set -eu

usage() {
  printf '%s\n' \
    'Usage:' \
    '  install-claude.sh --global' \
    '  install-claude.sh --project /path/to/project'
}

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
source_dir="$script_dir/../verstak"

if [ "$#" -eq 1 ] && [ "$1" = "--global" ]; then
  target_parent="$HOME/.claude/skills"
elif [ "$#" -eq 2 ] && [ "$1" = "--project" ]; then
  if [ ! -d "$2" ]; then
    printf 'Project directory not found: %s\n' "$2" >&2
    exit 1
  fi
  target_parent="$2/.claude/skills"
else
  usage
  exit 2
fi

target_dir="$target_parent/verstak"

if [ ! -f "$source_dir/SKILL.md" ]; then
  printf 'Source skill not found: %s\n' "$source_dir" >&2
  exit 1
fi

if [ -e "$target_dir" ]; then
  printf 'Target already exists: %s\n' "$target_dir" >&2
  printf '%s\n' 'Remove or rename it explicitly before reinstalling.' >&2
  exit 1
fi

mkdir -p "$target_parent"
cp -R "$source_dir" "$target_dir"

printf 'Installed verstak for Claude Code: %s\n' "$target_dir"
printf '%s\n' 'Open Claude Code and run /verstak or /skills to verify.'
