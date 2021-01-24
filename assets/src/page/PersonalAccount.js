import React, { useRef, useEffect, useContext } from 'react';
import { Container, Row } from 'react-bootstrap';
import { PersonalAccountContext } from '../state/personalAccountState/PersonalAccountContext';
import AccountForm from '../components/account/AccountForm';
import AddAccount from '../components/account/AddAccount';

const PersonalAccount = () => {
  const {
    activeUser,
    changeUser,
    getUser,
    handleChangeAccount,
    handleSubmitAccount,
    handleChangeAvatar,
  } = useContext(PersonalAccountContext);

  const inputEl = useRef(null);
  useEffect(() => {
    getUser();
    // eslint-disable-next-line
  }, []);
  const { first_name, last_name, email, username, role, avatar } = activeUser;
  return (
    <Container className="p-3">
      <Row className="justify-content-md-center">
        <AddAccount
          first_name={first_name}
          last_name={last_name}
          email={email}
          username={username}
          avatar={avatar}
          role={role}
        />
        <AccountForm
          first_name={first_name}
          last_name={last_name}
          email={email}
          username={username}
          role={role}
          inputEl={inputEl}
          handleChangeAccount={handleChangeAccount}
          handleSubmitAccount={handleSubmitAccount}
          handleChangeAvatar={handleChangeAvatar}
          changeUser={changeUser}
        />
      </Row>
    </Container>
  );
};
export default PersonalAccount;
