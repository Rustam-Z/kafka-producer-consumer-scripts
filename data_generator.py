from faker import Faker

faker = Faker()


def get_registered_user():
    return {
        "name": faker.name(),
        "address": faker.address(),
        "created_at": faker.year()
    }


if __name__ == '__main__':
    print(get_registered_user())
