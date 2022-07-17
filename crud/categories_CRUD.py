import sqlite3
from schemes import CategoryScheme
from schemes.categories import CategoryInDBScheme

conn = sqlite3.connect("shop.db")
cur = conn.cursor()


class CategoryCRUD:

    @staticmethod
    def add(category: CategoryScheme):
        cur.execute("""
            INSERT INTO category(name, parent_id, is_published);
        """, (category.name, category.parent_id, category.is_published))
        conn.commit()

    @staticmethod
    def get(category_id: int) -> CategoryInDBScheme:
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
