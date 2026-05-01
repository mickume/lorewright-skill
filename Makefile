SKILL_NAME := lorewright
SKILL_DIR  := $(HOME)/.claude/skills
SKILL_SRC  := $(CURDIR)/.claude/skills/$(SKILL_NAME)

.PHONY: install uninstall

install:
	@mkdir -p $(SKILL_DIR)
	@ln -sfn $(SKILL_SRC) $(SKILL_DIR)/$(SKILL_NAME)
	@echo "Installed $(SKILL_NAME) → $(SKILL_DIR)/$(SKILL_NAME)"

uninstall:
	@rm -f $(SKILL_DIR)/$(SKILL_NAME)
	@echo "Removed $(SKILL_NAME) from $(SKILL_DIR)"
