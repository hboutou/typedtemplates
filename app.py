from typedtemplates import templates


def main():
    sql = templates.get_items(ids=(1,2,3), names=["foo","bar"])
    print(sql)


if __name__ == '__main__':
    main()
