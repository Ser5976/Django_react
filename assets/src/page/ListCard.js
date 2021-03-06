import React, { useEffect, useContext } from 'react';
import { Container, CardColumns, Row } from 'react-bootstrap';
import MyCard from '../components/MyCard';
import NumberingSystem from '../components/NumberingSystem';
import { BaseContext } from '../state/baseState/BaseContext';
import { RegistrationContext } from '../state/registrationState/RegistrationContext';
import { receiveDataStorage } from '../utilities/receiveDataStorage';

const ListCard = () => {
  const {
    itemList,
    refreshList,
    handleDelete,
    handleShow,
    editItem,
    count,
    pageSize,
    currentPage,
    pagination,
  } = useContext(BaseContext);
  const { rememberLastEvent } = useContext(RegistrationContext);
  useEffect(() => {
    // const url = ModelUrls.ITEMS;
    currentPage !== 1 && receiveDataStorage('urlPage') !== null
      ? refreshList(receiveDataStorage('urlPage'))
      : refreshList();

    // eslint-disable-next-line
  }, []);

  return (
    <>
      <Container fluid style={{ paddingTop: '2rem', paddingBottom: '2rem' }}>
        <CardColumns style={{ columnCount: 'auto' }}>
          {itemList.map((item) => {
            return (
              <MyCard
                key={item.id}
                price={item.price}
                photo={item.photo}
                handleDelete={handleDelete}
                item={item}
                handleShow={handleShow}
                editItem={editItem}
                rememberLastEvent={rememberLastEvent}
              />
            );
          })}
        </CardColumns>
      </Container>
      <div style={{ position: 'absolute', bottom: 0, width: '100%' }}>
        <hr />
        <Row className="justify-content-sm-center ">
          <NumberingSystem
            count={count}
            pageSize={pageSize}
            pagination={pagination}
            currentPage={currentPage}
          />
        </Row>
      </div>
    </>
  );
};
export default ListCard;
