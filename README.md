# Verstak / Верстак

- [Русский](#русский)
- [English](#english)

## Русский

«Верстак» — skill для pixel-perfect вёрстки экранов и компонентов по макетам Figma в Codex и OpenCode.

Исходники находятся в [`verstak/`](verstak/). Обе платформы используют один `SKILL.md`, поэтому инструкции не дублируются и не расходятся между версиями.

### Установка в OpenCode

Глобально:

```sh
./scripts/install-opencode.sh --global
```

В конкретный проект:

```sh
./scripts/install-opencode.sh --project /path/to/project
```

Проверить обнаружение:

```sh
cd /path/to/project
opencode debug skill
```

Папку `verstak` также можно скопировать вручную:

- в проект: `.opencode/skills/verstak`;
- глобально: `~/.config/opencode/skills/verstak`.

После обнаружения skill доступен как `/verstak` и может выбираться агентом автоматически по `description`.
Русские фразы «Верстак», «верстак», «сверстай по Figma», «сверстай экран по макету» и «сверстай компонент» сохранены как явные триггеры. Slash-команда остаётся `/verstak`, поскольку идентификаторы skills используют латиницу.

### Установка в Codex

Установите папку `verstak` как обычный Codex skill. Файл `verstak/agents/openai.yaml` содержит UI-метаданные Codex и безопасно игнорируется OpenCode.

## English

Verstak is a skill for implementing pixel-perfect screens and components from Figma designs in Codex and OpenCode.

The skill source lives in [`verstak/`](verstak/). Both platforms use the same `SKILL.md`, so instructions remain synchronized without duplication.

### Install in OpenCode

Globally:

```sh
./scripts/install-opencode.sh --global
```

For a specific project:

```sh
./scripts/install-opencode.sh --project /path/to/project
```

Verify discovery:

```sh
cd /path/to/project
opencode debug skill
```

You can also copy the `verstak` directory manually:

- project scope: `.opencode/skills/verstak`;
- global scope: `~/.config/opencode/skills/verstak`.

Once discovered, the skill is available as `/verstak` and may be selected automatically by the agent based on its `description`.
Russian prompts such as `Верстак`, `верстак`, `сверстай по Figma`, `сверстай экран по макету`, and `сверстай компонент` remain explicit triggers. The slash command stays `/verstak` because skill IDs use Latin characters.

### Install in Codex

Install the `verstak` directory as a regular Codex skill. The `verstak/agents/openai.yaml` file contains Codex UI metadata and is safely ignored by OpenCode.
