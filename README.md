
---

## 🧩 Maya & Blender 메뉴 등록 가이드 (README)

### 🐾 Maya에서 메뉴바에 등록하기

1. **패키지 설치**

```bash
pip install "gpclean@git+https://github.com/너의계정/gpclean.git"
```

2. **userSetup.py 설정**

Maya가 실행될 때 자동으로 메뉴를 등록하려면, `userSetup.py` 파일에 아래 코드를 추가합니다:

```python
# 경로: ~/Documents/maya/2024/scripts/userSetup.py

import gpclean.ui.menu
gpclean.ui.menu.create_menu()
```

> ❗ `gpclean.ui.menu.create_menu()`는 PySide6 UI를 메뉴바에 등록하는 함수입니다.

---

### 🧿 Blender에서 메뉴바에 등록하기

#### 1. 패키지 설치

```bash
pip install "gpclean@git+https://github.com/너의계정/gpclean.git"
```

#### 2. 애드온 수동 등록 (1회만)

Blender에서 Python 콘솔에 아래 코드를 입력합니다:

```python
import gpclean.blender.addon as addon
addon.register()
```

> ✅ 그러면 상단 메뉴에 `Launch GP Clean UI` 버튼이 생기고, 클릭 시 PySide6 UI가 실행됩니다.

#### 3. Blender 실행 시 자동으로 등록되게 하려면?

Blender의 `Text Editor`에 아래 코드를 입력 후 **Register**를 눌러 저장합니다:

```python
import gpclean.blender.addon as addon
addon.register()
```

> 또는 `Text Editor > New` 후 `.py` 파일로 저장하고, Preferences > Add-ons > Install... 메뉴로 등록할 수도 있습니다.

---

### 💡 참고

* `gpclean.main.launch_gp_clean()`은 PySide6 기반 UI를 실행하는 진입점입니다.
* `menu.create_menu()` 함수는 Maya 상단 메뉴에 커스텀 메뉴와 버튼을 추가합니다.
* Blender에서는 스레드를 사용해 UI 충돌 없이 PySide 창을 띄웁니다.

---