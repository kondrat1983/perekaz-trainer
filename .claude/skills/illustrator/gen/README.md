# Генераторы картинок

Все картинки творов, кроме «Щасливого принца», собраны этими скриптами в стиле аплікації.

- `paper.py` — кусок с тенью `P`, деталь `D`, полоска `S`, глаз `eye`.
- `human.py` — человек по описанию (`sex`, `age`, `skin`, `hair`, `outfit`, `outfit_type`, `headwear`, `beard`, `item`) и эмоции: neutral, happy, sad, angry, scared.
- `fox.py`, `animals.py`, `animals2.py` — звери и особые персонажи (русалка, фея, ельф, джин, відьма, лицар).
- `scenery.py`, `bgs.py` — фоны 600×400. `items.py` — предметы 200×200.
- `assemble.py plan.json` — план твору (персонажи, предметы, сцены) → `data/works/<id>/` и `images/<id>/` с автоматической расстановкой в кадре.

Запуск из корня репозитория: `python3 .claude/skills/illustrator/gen/assemble.py plan.json`. После этого обязательно рендер (`render.mjs`), `npm test` и подъём `CACHE` в `sw.js`.
