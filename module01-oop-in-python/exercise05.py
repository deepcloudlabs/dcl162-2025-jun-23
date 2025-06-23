from abc import abstractmethod, ABC


class SpellChecker(ABC):
    @abstractmethod
    def check(self, word: str) -> bool:
        pass


class TurkishSpellChecker(SpellChecker):
    def __init__(self, spell_dict):
        self.spell_dict = spell_dict

    def check(self, word: str) -> bool:
        return word in self.spell_dict


class FrenchSpellChecker(SpellChecker):
    def __init__(self, spell_dict):
        self.spell_dict = spell_dict

    def check(self, word: str) -> bool:
        return word in self.spell_dict


class SpanishSpellChecker(SpellChecker):
    def __init__(self, spell_dict):
        self.spell_dict = spell_dict

    def check(self, word: str) -> bool:
        return word in self.spell_dict


class Emailer:
    def __init__(self, email_dict, spell_checker: SpellChecker):
        self.email_dict = email_dict

    def send(self, email_message: str) -> bool:
        for word in email_message.split():
            if not self.spell_checker.check(word):
                return False
        # other tasks related to sending an email message...

        return True
