from .document_character import DocumentCharacter


# Flyweight Factory (Class) - creates and manages flyweight objects.
class LetterFactory:
    _character_cache = {}

    @classmethod
    def crate_letter(cls, character_value):
        if character_value in cls._character_cache:
            # if exists, return the cached character object.
            return cls._character_cache[character_value]
        else:
            # if not exists, create the character object and cache it.
            character_obj = DocumentCharacter(character_value, "Arial", 10)
            cls._character_cache[character_value] = character_obj
            return character_obj

    @classmethod
    def get_total_characters(cls):
        return len(cls._character_cache)
