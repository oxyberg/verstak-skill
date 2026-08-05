# Навык «Верстак»

Pixel-perfect вёрстка экранов и компонентов по макетам Figma для Codex и OpenCode.

Исходники skill находятся в [`verstak/`](verstak/). Один и тот же `SKILL.md` используется обеими платформами, поэтому логика не дублируется.

## OpenCode

Установить skill глобально:

```sh
./scripts/install-opencode.sh --global
```

Или установить только в конкретный проект:

```sh
./scripts/install-opencode.sh --project /path/to/project
```

Проверить обнаружение:

```sh
cd /path/to/project
opencode debug skill
```

OpenCode также позволяет установить папку `verstak` вручную:

- в проект: `.opencode/skills/verstak`;
- глобально: `~/.config/opencode/skills/verstak`.

После обнаружения skill доступен как `/verstak` и может выбираться агентом автоматически по `description`.

## Codex

Устанавливать папку `verstak` как обычный Codex skill. Файл `verstak/agents/openai.yaml` содержит UI-метаданные Codex и безопасно игнорируется OpenCode.
