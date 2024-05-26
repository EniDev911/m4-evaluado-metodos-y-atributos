from ingredientes import I_PROTEICOS, I_VEGETALES, T_MASA


class Pizza:

    precio = 10000
    tamanio = "familiar"

    @staticmethod
    def validar(elemento: str, opciones: list) -> bool:
        return False if elemento not in opciones else True

    def ordenar(self):

        self.proteico = input(
            f"Ingresa el ingrediente proteico {I_PROTEICOS}: "
        ).lower()
        self.vegetal1 = input(
            f"Ingresa el primer ingrediente vegetal {I_VEGETALES}: "
        ).lower()

        tmp_vegetales = I_VEGETALES.copy()
        (
            tmp_vegetales.remove(self.vegetal1)
            if Pizza.validar(self.vegetal1, tmp_vegetales)
            else 0
        )

        self.vegetal2 = input(
            f"Ingresa el segundo ingrediente vegetal {tmp_vegetales}: "
        ).lower()

        self.t_masa = input(f"Ingresa el tipo de masa {T_MASA}: ")

        self.es_valido = (
            Pizza.validar(self.proteico, I_PROTEICOS)
            and Pizza.validar(self.vegetal1, I_VEGETALES)
            and Pizza.validar(self.vegetal2, I_VEGETALES)
            and Pizza.validar(self.t_masa, T_MASA)
        )


if __name__ == "__main__":
    p = Pizza()
    p.ordenar()
    print(p.es_valido)
