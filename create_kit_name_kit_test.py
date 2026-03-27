import sender_stand_request
import data


# --- FUNCIONES DE APOYO ---

def get_new_user_token():
    user_body = data.user_body.copy()
    response = sender_stand_request.post_new_user(user_body)
    return response.json().get("authToken")


def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.crear_kit_personal(kit_body, auth_token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.crear_kit_personal(kit_body, auth_token)

    assert response.status_code == 400


# --- LISTA DE COMPROBACIÓN (9 PRUEBAS) ---

# Prueba 1: 1 carácter
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = data.kit_body.copy()
    kit_body["name"] = "a"
    positive_assert(kit_body)


# Prueba 2: 511 caracteres
def test_create_kit_511_letter_in_name_get_success_response():
    kit_body = data.kit_body.copy()
    kit_body["name"] = ("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                        "abcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                        "abcdabcdabcdabC")
    positive_assert(kit_body)


# Prueba 3: 0 caracteres
def test_create_kit_empty_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body["name"] = ""
    negative_assert_code_400(kit_body)


# Prueba 4: 512 caracteres
def test_create_kit_512_letter_in_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body["name"] = ("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                        "abcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                        "abcdabcdabcdabcD")
    negative_assert_code_400(kit_body)


# Prueba 5: Caracteres especiales
def test_create_kit_special_symbol_name_get_success_response():
    kit_body = data.kit_body.copy()
    kit_body["name"] = "№%@"
    positive_assert(kit_body)


# Prueba 6: Espacios
def test_create_kit_has_spaces_in_name_get_success_response():
    kit_body = data.kit_body.copy()
    kit_body["name"] = " A Aaa "
    positive_assert(kit_body)


# Prueba 7: Números (como string)
def test_create_kit_has_number_in_name_get_success_response():
    kit_body = data.kit_body.copy()
    kit_body["name"] = "123"
    positive_assert(kit_body)


# Prueba 8: Parámetro ausente
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)


# Prueba 9: Tipo de parámetro incorrecto (número)
def test_create_kit_number_type_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body["name"] = 123
    negative_assert_code_400(kit_body)