import sqlite3
from schemes.categories import CategoryScheme
from schemes.categories import CategoryInDBScheme

conn = sqlite3.connect("shop.db")
cur = conn.cursor()


class CategoryCRUD:

    @staticmethod
    def add(category: CategoryScheme) -> None:
        cur.execute("""
            INSERT INTO category(name, parent_id, is_published)
            VALUES(?, ?, ?);
        """, (category.name, category.parent_id, category.is_published))
        conn.commit()

    @staticmethod
    def get(category_id: CategoryScheme) -> CategoryInDBScheme:
        cur.execute(f"""
            SELECT * FROM categories WHERE id = {category_id}
        """)
        result = cur.fetchone()
        category = CategoryInDBScheme(
            id=result[0],
            parent_id=result[1],
            is_published=result[2],
            name=result[3]
        )
        return category

    @staticmethod
    def get_all() -> list[CategoryInDBScheme]:
        cur.execute("""
        SELECT * FROM categories
        """)
        result = cur.fetchall()
        return result

    @staticmethod
    def update(category_id: int, category: CategoryScheme) -> None:
        cur.execute(f"""
        UPDATE categories SET
        parent_id={category.parent_id}
        is_published={category.is_published}
        name={category.name}
        WHERE id = {category_id}
        """)
        conn.commit()

    @staticmethod
    def delete(category_id: int) -> None:
        cur.execute(f"""
        DELETE FROM categories WHERE id = {category_id}
        """)
        conn.commit()
