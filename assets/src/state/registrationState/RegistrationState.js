import React, { useReducer } from 'react';
import axios from 'axios';
import { RegistrationContext } from './RegistrationContext';
import { authReducer } from '../../reducers/reducers';
import { AuthUrls } from '../../constants/urls';

const initialState = {
  activeUsers: {
    email: '',
    username: '',
    password1: '',
    password2: '',
    role: undefined,
  },
  validated: false,
  show: false,
};

const RegistrationState = ({ children }) => {
  const [state, dispatch] = useReducer(authReducer, initialState);
  const handleClose = () => dispatch({ type: 'SHOW_CLOSE' });
  const { activeUsers, validated, show } = state;
  const handleRegistrationShow = () => {
    dispatch({ type: 'SHOW_CLOSE' });
    const emptyActiveUsers = {
      activeUsers: {
        email: '',
        username: '',
        password1: '',
        password2: '',
        role: undefined,
      },
    };
    dispatch({
      type: 'AUTH_CLEAR',
      payload: { ...emptyActiveUsers.activeUsers },
    });
  };

  const handleChangeInput = (e) => {
    const inputValue = {
      ...state.activeUsers,
      [e.target.name]: e.target.value,
    };
    dispatch({
      type: 'CHANGE_INPUT_VALUE',
      payload: inputValue,
    });
  };
  // console.log(activeUsers);
  const handleSubmitForm = async (event) => {
    event.preventDefault();

    const form = event.currentTarget;
    if (form.checkValidity() === true) {
      event.stopPropagation();
      // console.log(activeUsers);
      const response = await axios.post(AuthUrls.REGISTRATION, activeUsers);
      console.log(response);
      console.log(response.config.data.username);
      let token = response.data['key'];
      localStorage.setItem('token', token);
      dispatch({ type: 'SHOW_CLOSE' });
    }

    dispatch({ type: 'VALIDATED' });
  };

  return (
    <RegistrationContext.Provider
      value={{
        activeUsers,
        validated,
        show,
        handleChangeInput,
        handleSubmitForm,
        handleRegistrationShow,
        handleClose,
      }}
    >
      {children}
    </RegistrationContext.Provider>
  );
};

export default RegistrationState;
