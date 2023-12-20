# utils.py
from alembic.operations import Operations
from sqlalchemy import text


def create_update_modified_column_function(op: Operations):
    op.execute(
        """
        CREATE OR REPLACE FUNCTION update_modified_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = now();
            RETURN NEW;
        END;
        $$ language 'plpgsql';
        """
    )


def drop_update_modified_column_function(op: Operations):
    op.execute("DROP FUNCTION update_modified_column")


def create_update_timestamp_trigger(op: Operations, table_name: str):
    trigger_sql = f"""
    CREATE TRIGGER update_timestamp_{table_name}
    BEFORE UPDATE ON {table_name}
    FOR EACH ROW
    EXECUTE FUNCTION update_modified_column();
    """
    op.execute(text(trigger_sql))
