Only directive Test
=====================

.. only:: tag_a

    .. req:: req_001

       I shall not appear if not running tag_a

.. only:: tag_b

    .. req:: req_002

       I shall not appear if not running tag_b

.. only:: tag_a or tag_b

    .. req:: req_003

       I shall not appear if not running either tag_a or tag_b
       

.. req:: req_004

       I shall always appear


.. needtable::
    types: req
