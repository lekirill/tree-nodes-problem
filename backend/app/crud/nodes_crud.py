from typing import List, Dict

from app.clients.db import DBClient


async def get_node(db: DBClient, node_id: int) -> Dict:
    result = await db.first("""
    SELECT node_id, "value", parent_id, is_deleted
    FROM public.database
    WHERE node_id = $1 AND is_deleted = False
    """, (node_id,))
    return dict(result) if result else {}


async def get_all_nodes(db: DBClient) -> List[Dict]:
    result = await db.select("""
    SELECT node_id, "value", parent_id, is_deleted
    FROM public.database
    """, ())
    prepared_data = []
    for row in result:
        prepared_data.append(dict(row))
    return prepared_data


async def update_node(db: DBClient, node: Dict) -> None:
    await db.update("""
    UPDATE public."database"
    SET "value"=$2, 
        updated_at=NOW()
    WHERE node_id=$1;
    """, (node['node_id'], node['value'],))


async def delete_node(db: DBClient, node: Dict) -> None:
    data = await db.select("""
               WITH RECURSIVE c AS (
               SELECT node_id 
               from public."database" 
               where parent_id = $1
               UNION ALL
               SELECT sa.node_id 
               from public."database" AS sa
                  JOIN c ON c.node_id = sa.parent_id
            )
            SELECT node_id FROM c;
        """, (node['node_id'],))

    nodes_to_delete = [node['node_id']]
    for n in data:
        nodes_to_delete.append(n['node_id'])
    await db.update("""
        UPDATE public."database"
        SET is_deleted=True, 
            deleted_at=NOW(),
            updated_at=NOW()
        WHERE node_id = ANY($1);
        """, (nodes_to_delete,))


async def insert_node(db: DBClient, node: Dict) -> int:
    data = await db.insert("""
                INSERT INTO public."database"
                (parent_id, "value")
                VALUES($1, $2)
                RETURNING node_id;
   """, (node['parent_id'], node['value']))
    new_node_id = data['node_id']
    return new_node_id


async def reset(db: DBClient) -> None:
    await db.delete("""
    TRUNCATE TABLE public."database"; 
    """, ())
    await db.delete("""
        ALTER SEQUENCE public.node_seq RESTART WITH 1;  
        """, ())
    await db.delete("""
        INSERT INTO public.database (parent_id, "value")
    VALUES (NULL, 'value_1'),
        (1, 'value_2'),
        (1, 'value_3'),
        (1, 'value_4'),
        (2, 'value_5'),
        (2, 'value_6'),
        (2, 'value_7'),
        (5, 'value_8'),
        (5, 'value_9'),
        (8, 'value_10'),
        (1, 'value_11'),
        (11, 'value_12'),
        (12, 'value_13'),
        (13, 'value_14');
        """, ())
