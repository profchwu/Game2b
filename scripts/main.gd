extends Node3D

enum Screen { TITLE, LEVEL, RESULT }

const ROOM_SAVINGS := "res://assets/blender/exports/savings-room.glb"
const ROOM_GARDEN := "res://assets/blender/exports/mist-garden.glb"
const CHARACTER_SCENE := "res://assets/blender/exports/dream-keeper.glb"

const LEVELS := [
	{
		"title": "第一關｜夢想種子",
		"chapter": "先照顧需要，再為願望存錢",
		"story": "今天要買一把 2 枚夢幣的澆水壺；下週想要的月光風箏要 6 枚。你有 8 枚夢幣，怎麼安排？",
		"answers": [
			"8 枚都買風箏，今天先不買澆水壺",
			"先留 2 枚買澆水壺，把 6 枚存起來",
			"8 枚全存起來，今天也不買需要的澆水壺"
		],
		"correct": 1,
		"success": "安排得很好！先照顧今天的需要，再把剩下的錢存向目標。你取得了夢想鑰匙。",
		"retry": "再想想：今天的需要要先照顧，願望可以慢慢存。"
	},
	{
		"title": "第二關｜霧中種子",
		"chapter": "認識投資的變化與風險",
		"story": "4 顆夢種子要為遙遠的目標慢慢長大。兩塊苗圃都可能遇到不好的季節。哪種安排能避免把所有希望放在同一塊苗圃？",
		"answers": [
			"4 顆都種在月豆田；它一定收成最好",
			"2 顆種月豆田、2 顆種星花田；分散可以降低集中風險，但仍可能收成不好",
			"2 顆種月豆田、2 顆種星花田；分散後就保證不會損失"
		],
		"correct": 1,
		"success": "答對了！分散能降低把所有種子放在一處的風險，但不能保證不會損失。你取得了成長鑰匙。",
		"retry": "再看看兩個說法：投資結果會變動，分散也不能保證一定有收穫。"
	}
]

var current_screen: Screen = Screen.TITLE
var current_level := 0
var level_scores := [0, 0]
var attempts := [0, 0]
var keys := [false, false]
var reduced_motion := false

var room_instance: Node3D
var character_instance: Node3D
var animation_player: AnimationPlayer
var camera: Camera3D

var ui_root: Control
var header_title: Label
var header_score: Label
var header_keys: Label
var motion_button: Button
var main_panel: PanelContainer
var panel_content: VBoxContainer

var font_file := FontFile.new()


func _ready() -> void:
	font_file.load_dynamic_font("res://assets/fonts/NotoSansTC-VF.ttf")
	_build_world()
	_build_ui()
	_show_title()
	_load_room(ROOM_SAVINGS)


func _build_world() -> void:
	camera = Camera3D.new()
	camera.name = "GameCamera"
	camera.position = Vector3(0.0, 7.0, 16.0)
	camera.fov = 48.0
	add_child(camera)
	camera.look_at(Vector3(0.0, 2.4, 0.0), Vector3.UP)
	camera.current = true

	var environment := WorldEnvironment.new()
	var world := Environment.new()
	world.background_mode = Environment.BG_COLOR
	world.background_color = Color("11140f")
	world.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	world.ambient_light_color = Color("8a8d70")
	world.ambient_light_energy = 0.58
	world.tonemap_mode = Environment.TONE_MAPPER_FILMIC
	environment.environment = world
	add_child(environment)

	var key_light := DirectionalLight3D.new()
	key_light.name = "Warm room light"
	key_light.rotation_degrees = Vector3(-42, -28, 0)
	key_light.light_color = Color("ffd49a")
	key_light.light_energy = 1.15
	key_light.shadow_enabled = true
	add_child(key_light)

	var fill_light := DirectionalLight3D.new()
	fill_light.name = "Soft garden fill"
	fill_light.rotation_degrees = Vector3(-25, 145, 0)
	fill_light.light_color = Color("b5d2cb")
	fill_light.light_energy = 0.34
	fill_light.shadow_enabled = false
	add_child(fill_light)


func _build_ui() -> void:
	ui_root = Control.new()
	ui_root.name = "GameUI"
	ui_root.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	ui_root.mouse_filter = Control.MOUSE_FILTER_PASS
	add_child(ui_root)

	var vignette := ColorRect.new()
	vignette.color = Color(0.025, 0.035, 0.028, 0.22)
	vignette.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	vignette.mouse_filter = Control.MOUSE_FILTER_IGNORE
	ui_root.add_child(vignette)

	var header := PanelContainer.new()
	header.name = "StatusHeader"
	header.anchor_left = 0.035
	header.anchor_top = 0.025
	header.anchor_right = 0.965
	header.anchor_bottom = 0.14
	header.add_theme_stylebox_override("panel", _panel_style(Color(0.055, 0.07, 0.058, 0.9), Color("b89a5d"), 12))
	ui_root.add_child(header)

	var header_margin := MarginContainer.new()
	header_margin.add_theme_constant_override("margin_left", 20)
	header_margin.add_theme_constant_override("margin_right", 20)
	header_margin.add_theme_constant_override("margin_top", 10)
	header_margin.add_theme_constant_override("margin_bottom", 10)
	header.add_child(header_margin)

	var header_row := HBoxContainer.new()
	header_row.add_theme_constant_override("separation", 18)
	header_margin.add_child(header_row)

	header_title = _label("小小夢魔　／　霧中種子園", 22, Color("f2e6c8"))
	header_title.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	header_row.add_child(header_title)

	header_score = _label("得分　0 / 200", 18, Color("f0c86b"))
	header_score.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	header_row.add_child(header_score)

	header_keys = _label("KEY 1　鎖定　　KEY 2　鎖定", 15, Color("c1b99f"))
	header_keys.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	header_row.add_child(header_keys)

	motion_button = Button.new()
	motion_button.text = "動態：開"
	motion_button.custom_minimum_size = Vector2(128, 48)
	_apply_button_style(motion_button, true)
	motion_button.pressed.connect(_toggle_motion)
	header_row.add_child(motion_button)

	main_panel = PanelContainer.new()
	main_panel.name = "MainPanel"
	main_panel.anchor_left = 0.035
	main_panel.anchor_top = 0.22
	main_panel.anchor_right = 0.965
	main_panel.anchor_bottom = 0.955
	main_panel.add_theme_stylebox_override("panel", _panel_style(Color(0.055, 0.068, 0.056, 0.93), Color("b89a5d"), 18))
	ui_root.add_child(main_panel)

	var content_margin := MarginContainer.new()
	content_margin.add_theme_constant_override("margin_left", 28)
	content_margin.add_theme_constant_override("margin_right", 28)
	content_margin.add_theme_constant_override("margin_top", 20)
	content_margin.add_theme_constant_override("margin_bottom", 20)
	main_panel.add_child(content_margin)

	panel_content = VBoxContainer.new()
	panel_content.add_theme_constant_override("separation", 10)
	content_margin.add_child(panel_content)


func _label(value: String, size: int, color: Color) -> Label:
	var result := Label.new()
	result.text = value
	result.add_theme_font_override("font", font_file)
	result.add_theme_font_size_override("font_size", size)
	result.add_theme_color_override("font_color", color)
	result.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	return result


func _panel_style(background: Color, border: Color, radius: int) -> StyleBoxFlat:
	var style := StyleBoxFlat.new()
	style.bg_color = background
	style.border_color = border
	style.set_border_width_all(1)
	style.set_corner_radius_all(radius)
	style.shadow_color = Color(0, 0, 0, 0.42)
	style.shadow_size = 12
	style.content_margin_left = 12
	style.content_margin_right = 12
	style.content_margin_top = 8
	style.content_margin_bottom = 8
	return style


func _apply_button_style(button: Button, secondary: bool = false) -> void:
	button.add_theme_font_override("font", font_file)
	button.add_theme_font_size_override("font_size", 18)
	button.add_theme_color_override("font_color", Color("f3ead5"))
	button.add_theme_color_override("font_hover_color", Color("fff4d7"))
	button.add_theme_color_override("font_pressed_color", Color("fff4d7"))
	button.add_theme_color_override("font_disabled_color", Color("a7a18d"))
	button.add_theme_stylebox_override("normal", _panel_style(Color(0.12, 0.145, 0.11, 0.96) if not secondary else Color(0.09, 0.11, 0.09, 0.94), Color("85754c"), 10))
	button.add_theme_stylebox_override("hover", _panel_style(Color(0.18, 0.20, 0.13, 0.98), Color("e0bd6c"), 10))
	button.add_theme_stylebox_override("pressed", _panel_style(Color(0.20, 0.16, 0.09, 0.98), Color("f0c86b"), 10))
	button.add_theme_stylebox_override("disabled", _panel_style(Color(0.10, 0.12, 0.10, 0.84), Color("756c51"), 10))
	button.add_theme_constant_override("outline_size", 0)
	button.custom_minimum_size.y = 56
	button.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	button.focus_mode = Control.FOCUS_ALL


func _clear_panel() -> void:
	for child in panel_content.get_children():
		child.queue_free()


func _show_title() -> void:
	current_screen = Screen.TITLE
	_clear_panel()
	var spacer := Control.new()
	spacer.custom_minimum_size.y = 8
	panel_content.add_child(spacer)
	var eyebrow := _label("DREAM GARDEN　✦　小小夢境理財課", 14, Color("e2c478"))
	eyebrow.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	panel_content.add_child(eyebrow)
	var title := _label("霧中種子園", 34, Color("f4e8ca"))
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	panel_content.add_child(title)
	var description := _label("在兩座夢境花園裡練習存錢，認識投資的變化與風險。\n答對就取得 KEY，完成後看看這次的練習成果。", 18, Color("d1cbb9"))
	description.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	description.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	panel_content.add_child(description)
	var start := Button.new()
	start.text = "進入花園　→"
	start.custom_minimum_size = Vector2(250, 60)
	_apply_button_style(start)
	start.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	start.pressed.connect(_start_game)
	panel_content.add_child(start)
	_update_hud()


func _start_game() -> void:
	current_level = 0
	level_scores = [0, 0]
	attempts = [0, 0]
	keys = [false, false]
	_update_hud()
	_show_level(0)
	_load_room(ROOM_SAVINGS)
	_play_animation("Idle")


func _show_level(level_index: int) -> void:
	current_level = level_index
	current_screen = Screen.LEVEL
	_clear_panel()
	var data: Dictionary = LEVELS[level_index]
	var chapter := _label("第 %d 關　／　%s" % [level_index + 1, data["chapter"]], 14, Color("e5c876"))
	panel_content.add_child(chapter)
	var title := _label(data["title"], 28, Color("f4e8ca"))
	panel_content.add_child(title)
	var prompt := _label(data["story"], 18, Color("ded8c8"))
	prompt.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	prompt.custom_minimum_size.y = 58
	panel_content.add_child(prompt)
	var level_score := _label("本關得分　%d / 100" % level_scores[level_index], 15, Color("f0c86b"))
	level_score.name = "LevelScore"
	panel_content.add_child(level_score)
	var answers: Array = data["answers"]
	for i in range(answers.size()):
		var answer := Button.new()
		answer.text = "　%d　%s" % [i + 1, answers[i]]
		answer.alignment = HORIZONTAL_ALIGNMENT_LEFT
		answer.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
		answer.custom_minimum_size.y = 58
		_apply_button_style(answer, true)
		answer.pressed.connect(_on_answer.bind(i))
		panel_content.add_child(answer)
	var feedback := _label("選一個安排，看看花園會怎麼回應。", 15, Color("c6bea9"))
	feedback.name = "Feedback"
	feedback.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	feedback.custom_minimum_size.y = 30
	panel_content.add_child(feedback)
	var next_button := Button.new()
	next_button.name = "ContinueButton"
	next_button.text = "前往下一座花園　→" if level_index == 0 else "查看本次練習成果　→"
	next_button.custom_minimum_size = Vector2(270, 52)
	_apply_button_style(next_button)
	next_button.size_flags_horizontal = Control.SIZE_SHRINK_END
	next_button.visible = false
	next_button.pressed.connect(_continue_after_level)
	panel_content.add_child(next_button)
	_update_hud()
	if level_index == 0:
		_load_room(ROOM_SAVINGS)
	else:
		_load_room(ROOM_GARDEN)
	_play_animation("Idle")


func _on_answer(answer_index: int) -> void:
	if current_screen != Screen.LEVEL:
		return
	attempts[current_level] += 1
	var data: Dictionary = LEVELS[current_level]
	var feedback: Label = panel_content.get_node("Feedback")
	if answer_index == int(data["correct"]):
		level_scores[current_level] = 100 if attempts[current_level] == 1 else 80
		keys[current_level] = true
		var level_score: Label = panel_content.get_node("LevelScore")
		level_score.text = "本關得分　%d / 100" % level_scores[current_level]
		feedback.text = String(data["success"])
		feedback.add_theme_color_override("font_color", Color("e8d081"))
		var next_button: Button = panel_content.get_node("ContinueButton")
		next_button.visible = true
		for child in panel_content.get_children():
			if child is Button and child != next_button:
				child.disabled = true
		_play_animation("Reach")
		_update_hud()
	else:
		feedback.text = String(data["retry"])
		feedback.add_theme_color_override("font_color", Color("e3c993"))
		_play_animation("Idle")


func _continue_after_level() -> void:
	if current_level == 0 and keys[0]:
		_show_level(1)
	elif current_level == 1 and keys[1]:
		_show_result()


func _show_result() -> void:
	current_screen = Screen.RESULT
	_clear_panel()
	var eyebrow := _label("本次練習成果", 15, Color("e2c478"))
	eyebrow.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	panel_content.add_child(eyebrow)
	var title := _label("兩把鑰匙，兩個新發現", 30, Color("f4e8ca"))
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	panel_content.add_child(title)
	var score_total: int = int(level_scores[0]) + int(level_scores[1])
	var score_line := _label("第一關　%d 分　　　第二關　%d 分　　　總分　%d / 200" % [level_scores[0], level_scores[1], score_total], 20, Color("f0c86b"))
	score_line.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	panel_content.add_child(score_line)
	var progress := ProgressBar.new()
	progress.min_value = 0
	progress.max_value = 200
	progress.value = score_total
	progress.show_percentage = false
	progress.custom_minimum_size.y = 18
	panel_content.add_child(progress)
	var recap := _label("你練習了先照顧需要、再為目標儲蓄；也看見分散選擇能降低集中風險，但不能保證不會損失。", 18, Color("ddd6c5"))
	recap.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	recap.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	panel_content.add_child(recap)
	var complete := _label("完成練習　2 / 2　　　取得 KEY　%d / 2" % [int(keys[0]) + int(keys[1])], 16, Color("c7d39e"))
	complete.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	panel_content.add_child(complete)
	var restart := Button.new()
	restart.text = "再走一次夢境　↺"
	restart.custom_minimum_size = Vector2(270, 56)
	_apply_button_style(restart)
	restart.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	restart.pressed.connect(_start_game)
	panel_content.add_child(restart)
	_update_hud()
	_play_animation("KeyUnlock")


func _update_hud() -> void:
	if not is_instance_valid(header_title):
		return
	header_score.text = "得分　%d / 200" % [level_scores[0] + level_scores[1]]
	var key_one := "已取得" if keys[0] else "鎖定"
	var key_two := "已取得" if keys[1] else "鎖定"
	header_keys.text = "KEY 1　%s　　KEY 2　%s" % [key_one, key_two]
	motion_button.text = "動態：關" if reduced_motion else "動態：開"


func _toggle_motion() -> void:
	reduced_motion = not reduced_motion
	if reduced_motion:
		if is_instance_valid(animation_player):
			animation_player.stop()
	else:
		_play_animation("Idle")
	_update_hud()


func _load_room(path: String) -> void:
	if is_instance_valid(room_instance):
		room_instance.queue_free()
	var packed := load(path) as PackedScene
	if packed == null:
		push_error("Could not load room scene: " + path)
		return
	room_instance = packed.instantiate() as Node3D
	room_instance.name = "CurrentRoom"
	add_child(room_instance)
	if not is_instance_valid(character_instance):
		var character_packed := load(CHARACTER_SCENE) as PackedScene
		if character_packed == null:
			push_error("Could not load dream keeper character")
			return
		character_instance = character_packed.instantiate() as Node3D
		character_instance.name = "DreamKeeper"
		character_instance.position = Vector3(-3.0, 0.0, -0.6)
		add_child(character_instance)
		animation_player = _find_animation_player(character_instance)
		_play_animation("Idle")


func _find_animation_player(node: Node) -> AnimationPlayer:
	if node is AnimationPlayer:
		return node as AnimationPlayer
	for child in node.get_children():
		var found := _find_animation_player(child)
		if found != null:
			return found
	return null


func _play_animation(animation_name: String) -> void:
	if reduced_motion or not is_instance_valid(animation_player):
		return
	var names := animation_player.get_animation_list()
	for name in names:
		if String(name).ends_with(animation_name):
			animation_player.play(name)
			return
