from typing import Union


from .models import (
    LiveBeganEvent,
    LiveBeganEventData,
    LiveEndedEvent,
    LiveEndedEventData,
    RoomChangeEvent,
    RoomChangeEventData,
    RecordingStartedEvent,
    RecordingStartedEventData,
    RecordingFinishedEvent,
    RecordingFinishedEventData,
    RecordingCancelledEvent,
    RecordingCancelledEventData,
    VideoFileCreatedEvent,
    VideoFileCreatedEventData,
    VideoFileCompletedEvent,
    VideoFileCompletedEventData,
    DanmakuFileCreatedEvent,
    DanmakuFileCreatedEventData,
    DanmakuFileCompletedEvent,
    DanmakuFileCompletedEventData,
    RawDanmakuFileCreatedEvent,
    RawDanmakuFileCreatedEventData,
    RawDanmakuFileCompletedEvent,
    RawDanmakuFileCompletedEventData,
    VideoPostprocessingCompletedEvent,
    VideoPostprocessingCompletedEventData,
    SpaceNoEnoughEvent,
    SpaceNoEnoughEventData,
    Error,
    ErrorData,
)


Event = Union[
    LiveBeganEvent,
    LiveEndedEvent,
    RoomChangeEvent,
    RecordingStartedEvent,
    RecordingFinishedEvent,
    RecordingCancelledEvent,
    VideoFileCreatedEvent,
    VideoFileCompletedEvent,
    DanmakuFileCreatedEvent,
    DanmakuFileCompletedEvent,
    RawDanmakuFileCreatedEvent,
    RawDanmakuFileCompletedEvent,
    VideoPostprocessingCompletedEvent,
    SpaceNoEnoughEvent,
    Error,
]

EventData = Union[
    LiveBeganEventData,
    LiveEndedEventData,
    RoomChangeEventData,
    RecordingStartedEventData,
    RecordingFinishedEventData,
    RecordingCancelledEventData,
    VideoFileCreatedEventData,
    VideoFileCompletedEventData,
    DanmakuFileCreatedEventData,
    DanmakuFileCompletedEventData,
    RawDanmakuFileCreatedEventData,
    RawDanmakuFileCompletedEventData,
    VideoPostprocessingCompletedEventData,
    SpaceNoEnoughEventData,
    ErrorData,
]
